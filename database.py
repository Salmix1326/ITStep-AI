from langchain_google_genai import GoogleGenerativeAIEmbeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_core.documents import Document
import os
import dotenv
import json
from uuid import uuid4

# завантаження апі ключа
dotenv.load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")

# модель для кодування текстів(embedding model)
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key=gemini_api_key
)

# створення весторної бази даних
pc = Pinecone(api_key=pinecone_api_key)
index_name = "soup"  # назва бази даних

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=768,      # кількість чисел при кодування
        metric="cosine",    # формула для схожості
        spec=ServerlessSpec(
            cloud="aws",         # хмарний сервер(амазон)
            region="us-east-1"   # регіон(Каліфорнія)
        ),
    )

index = pc.Index(index_name)
vector_store = PineconeVectorStore(
    index=index,
    embedding=embeddings
)

#работа с файлом
with open("data/lesson_rag/huge_file.txt", 'r', encoding="utf-8") as file:
    huge_file_text = file.read()

file_split_blocks = huge_file_text.split("\n\n\n")
file_split_block_titles = []

for block in file_split_blocks:
    block_parts = block.split("\n")
    block_title = block_parts[0]
    file_split_block_titles.append(block_title)

docs = []

# # створення документів
for i in range(len(file_split_blocks)):
    doc = Document(
        page_content=file_split_blocks[i],   # вміст дукумента
        metadata={                           # додаткова інформація
            "file name": "Условия гугл",
            "block title": file_split_block_titles[i],
            "author": "Google Programmer",
        }
    )

    docs.append(doc)

# # створення унікальних id для документів
ids = [str(uuid4()) for _ in range(len(docs))]

# завантаження документів у базу даних
# vector_store.add_documents(
#     documents=docs,
#     ids=ids
# )

# добавление id
id_map = {

}

for doc,id  in  zip(docs, ids):
    id_map[doc.metadata["block title"]] = id

with open ('ids.json', 'w', encoding="utf-8") as f:
    json.dump(id_map, f, indent=2, ensure_ascii=False)

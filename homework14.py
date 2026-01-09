# Модуль 3. Generative AI, LLM
# Тема: Langchain. Частина 6
# =============================================================================================
# Завдання 1
# Добавте в створену базу даних файл
# data/lesson_rag/huge_file.txt про умови користування гуглом
# Оскільки файл надто великий, то його треба добавляти частинами.
# Для цього:
# прочитайте вміст файлу
# розділіть його на окремі блоки(між блоками два порожніх рядка, дивись файл)
# отримайте перший рядок кожного блоку – це його назва
# створіть документи для кожного блоку.
# В метаданих:
# назва файлу
# назва блоку
# створіть ID та добавте все в існуючу базу даних
# добавте ID у json файл
# перевірте агента

import os
import dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
    trim_messages, BaseMessage
)

# завантаження апі ключа
dotenv.load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    api_key=gemini_api_key,
)

# модель для кодування текстів(embedding model)
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key=gemini_api_key
)

index_name = "soup"  # назва бази даних
pc = Pinecone(api_key=pinecone_api_key)
index = pc.Index(index_name)
vector_store = PineconeVectorStore(
    index=index,
    embedding=embeddings
)

# функция для поиска мест и сбора данных
def get_conditions_info(query: str) -> list:
    """
    Function for search information about google conditions
    Function returns list of similar information for user
    :param query:
    :return:
    """
    result_docs = vector_store.similarity_search(
        query,  # текст для порівняння схожості
        k=5,  # кількість документів у відповіді
    )

    return result_docs


# створення агента
agent = create_react_agent(
    model=llm,  # мовна модель
    tools=[get_conditions_info]
)

# історія повідомлень + інструкції
messages = [
    SystemMessage(
        """
        Ты - консультант Google.
        Пользователи будут спрашивать о условиях пользования.
        Тебе нужно рассказывать и консультировать их по разным вопросам.
        Для этого у тебя есть инструмент для поиска информации.
        Строго запрашивай данные из интструмента.
        Для лучшей работы - переводи запрос на украинский перед запросом в функцию, но отвечай на языке пользователя
        Если нужных данных данных не будет - скажи что данных таких нет и ты не можешь помочь.
        
        #ИНСТРУМЕНТЫ
        * get_conditions_info
        """
    )
]

while True:
    user_query = input("Ви: ")

    if user_query == '':
        break

    # переводимо str рядок у  HumanMessage
    human_message = HumanMessage(user_query)

    # добавляємо повідослення користувача до історії
    messages.append(human_message)

    # застосування агента
    # треба передавати словник
    input_data = {
        "messages": messages
    }

    response = agent.invoke(input_data)
    # response -- словник з усією історією + відповідь моделі

    # отримання всіє історії повідомлень
    messages = response['messages']

    # отримати фінальну відповідь моделі
    answer = messages[-1]
    print(answer.content)

    # # виведемння всієї історії
    print()
    print("Історія")

    for message in messages:
        print(repr(message))

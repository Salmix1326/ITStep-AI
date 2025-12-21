# Модуль 3. Generative AI, LLM
# Тема: Langchain. Частина 4
# Завдання 1
# ====================================================================================================
# Напишіть чат модель яка підсумовує всю розмову в декілька речень.
# Вкажіть щоб модель зберігала якомога більше деталей.
# Використайте цю модель для простого чат бота який замість trim_massages використовує модель з підсумуванням.
# Підсумовуйте повідомлення, коли їх більше 4.
# Старі повідомлення треба видалити
# НЕ ВИДАЛЯТИ SystemMessage та не використовувати його для підсумування
import os
import dotenv
from typing import List
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
    trim_messages,
    BaseMessage,
)


# завантаження апі ключа
dotenv.load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# створити llm
llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash-lite',
    api_key=api_key,
)

messages: List[BaseMessage] = [
    SystemMessage(f"""
   Ты - всезнающий чат, который может интересно рассказывать обо всем, что есть в мире.
    """)
]

trimmer = trim_messages(
    strategy='last',  # залишати останні повідомлення
    token_counter=len,  # рахуємо кількість повідомлень
    max_tokens=4,  # залишати максимум 5 повідомлення(System, AI, Human)
    start_on='human',  # історія завжди починатиметься з HumanMessage
    end_on='human',  # історія завжди закінчуватиметься з HumanMessage
    include_system=True  # SystemMessage не чіпати
)

chain = trimmer | llm
chat_history = messages[0]
count = 0

while True:
    user_query = input("Ваше сообщение: ")
    messages.append(HumanMessage(user_query))
    chat_history += f"User:{user_query}"
    count += 1

    if user_query == '':
        break

    response = chain.invoke(messages)
    messages.append(response)
    chat_history += f"AI:{response.content}"

    for m in messages:
        print(repr(m))

    print(f"AI: {response.content}")
    count += 1

    if count == 4:
        break

 # промпт
prompt = PromptTemplate.from_template(
    """
    Ты - помощник по суммированию и подытоживанию информации. 
    Тебе дадут историю чата. 
    Нужно сделать сводку и сохранить как можно больше важных деталей.
    Делай просто сводку по тексту без уточнения кто что говорил.
    
    #ИСТОРИЯ ЧАТА
    {history}
    """
)

 # створення ланцюга
chain = prompt | llm

result = chain.invoke({
    'history': chat_history,
})

print(f"Итог чата: {result.content}")

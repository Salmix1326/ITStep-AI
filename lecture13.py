# створення агентів
# агент -- чат-бот(llm) + інструменти
import os
import dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import GoogleSerperAPIWrapper
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
serper_api_key = os.getenv("SERPER_API_KEY")

# створити llm
llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    api_key=gemini_api_key,
)


# інструмент -- функція
# обов'язкова документація

# def product(a: int, b: int) -> int:
#     """
#     Множить 2 цілих числа то повертає їхній добуток
#
#     :param a: перше число
#     :param b: друге число
#     :return: добуток чисел
#     """
#     print("hello from product")
#     return a * b
#
#
# def get_weather(city: str, time: str) -> str:
#     """
#     Повертає інформацію про погоду у місті в певний час доби
#
#     :param city: назва міста
#     :param time: час доби(наприклад ранок, вечір, 10:30, 4 години дня)
#     :return: інформація про погоду
#     """
#     print("hello from get_weather")
#     return f"У {city} о {time} буде сонячно"
#
#
# # інструмент для пошуку в інтернеті
# searcher = GoogleSerperAPIWrapper(serper_api_key=serper_api_key)
#
#
# def search(query: str) -> str:
#     """
#     Шукає інформацію в інтернеті за запитом користувача
#
#     :param query: запит користувача
#     :return: результати пошуку
#     """
#
#     result = searcher.run(query) // run--results
#     print(result)
#
#     return result
#
#
# # створення агента
# agent = create_react_agent(
#     model=llm,  # мовна модель
#     tools=[product, get_weather, search]
# )
#
# # історія повідомлень + інструкції
#
# messages = [
#     SystemMessage(
#         """
#         Ти ввічлий чат-бот. Твоя задача давати інформативні та чіткі відповіді
#         на запити користувача.
#
#         У тебе є доступ до таких інструментів:
#         * product
#         * get_weather
#         * search
#         """
#     )
# ]
#
# while True:
#     user_query = input("Ви: ")
#
#     if user_query == '':
#         break
#
#     # переводимо str рядок у  HumanMessage
#     human_message = HumanMessage(user_query)
#
#     # добавляємо повідослення користувача до історії
#     messages.append(human_message)
#
#     # застосування агента
#     # треба передавати словник
#     input_data = {
#         "messages": messages
#     }
#
#     response = agent.invoke(input_data)
#     # response -- словник з усією історією + відповідь моделі
#
#     # отримання всіє історії повідомлень
#     messages = response['messages']
#
#     # отримати фінальну відповідь моделі
#     answer = messages[-1]
#     print(answer.content)
#
#     # виведемння всієї історії
#     print()
#     print("Історія")
#
#     for message in messages:
#         print(repr(message))

# Модуль 3. Generative AI, LLM
# Тема: Langchain. Частина 5
# Завдання 1
# ===================================================================================================
# Напишіть функцію яка перевіряє складність паролю:
# кількість символів(>8)
# наявність хоча б однієї літери\цифри\спеціального символу
# наявність літер в різних регістрах
# Функція повертає тест з описом паролю(що добре, а що погано)
# На основі цієї функції створіть агента.
# def check_password(password: str) -> dict:
#     """
#     Function for check password for various conditions
#     Function returns password info in dictionary style with password results
#     :param password:
#     :return:
#     """
#     password_info = {}
#
#     if len(password) <= 8:
#         password_info["password length"] = "Length must be greater than 8 symbols"
#
#     else:
#         password_info["password length"] = "Password is valid"
#
#     number_flag = False
#     alpha_flag = False
#     special_flag = False
#
#     for symbol in password:
#         if symbol.isalpha():
#             alpha_flag = True
#
#         elif symbol.isdigit():
#             number_flag = True
#
#         else:
#             special_flag = True
#
#     password_info["has_password_alpha"] = alpha_flag
#     password_info["has_password_digit"] = alpha_flag
#     password_info["has_password_special"] = alpha_flag
#
#     return password_info

# # створення агента
# agent = create_react_agent(
#     model=llm,  # мовна модель
#     tools=[check_password]
# )
#
# # історія повідомлень + інструкції
# messages = [
#     SystemMessage(
#         """
#         Ти вічливий чат-бот. Твоя задача давати інформативні та чіткі відповіді на запити користувача.
#         У тебе є доступ до таких інструментів:
#         * check_password
#         """
#     )
# ]
#
# while True:
#     user_query = input("Ви: ")
#
#     if user_query == '':
#         break
#
#     # переводимо str рядок у  HumanMessage
#     human_message = HumanMessage(user_query)
#
#     # добавляємо повідослення користувача до історії
#     messages.append(human_message)
#
#     # застосування агента
#     # треба передавати словник
#     input_data = {
#         "messages": messages
#     }
#
#     response = agent.invoke(input_data)
#     # response -- словник з усією історією + відповідь моделі
#
#     # отримання всіє історії повідомлень
#     messages = response['messages']
#
#     # отримати фінальну відповідь моделі
#     answer = messages[-1]
#     print(answer.content)
#
#     # виведемння всієї історії
#     print()
#     print("Історія")
#
#     for message in messages:
#         print(repr(message))

# Завдання 2
# ===================================================================================================
# Напишіть модель показує останні новини про певну людину.
# Якщо користувач вводить не ім’я людини, то вивести повідомлення «немає відповідної інформації»

# # інструмент для пошуку в інтернеті
# searcher = GoogleSerperAPIWrapper(serper_api_key=serper_api_key)
# def search_person(name: str) -> str:
#     """
#     Function search latest news about person with this name
#     Returns search results
#     :param name: person's name
#     :return: results
#     """
#     search_result = searcher.run(f"Latest news about {name}")
#
#     print(search_result)
#     return search_result
#
# # створення агента
# agent = create_react_agent(
#     model=llm,  # мовна модель
#     tools=[search_person]
# )
#
# # історія повідомлень + інструкції
# messages = [
#     SystemMessage(
#         """
#         Ти - вічливий чат-бот.
#         Твоя задача давати інформативні та чіткі відповіді на запити користувача.
#         Ты должен найти информацию о человеке в интернете.
#         У тебе є доступ до таких інструментів:
#         * search_person
#         """
#     )
# ]
#
# while True:
#     user_query = input("Ви: ")
#
#     if user_query == '':
#         break
#
#     # переводимо str рядок у  HumanMessage
#     human_message = HumanMessage(user_query)
#
#     # добавляємо повідослення користувача до історії
#     messages.append(human_message)
#
#     # застосування агента
#     # треба передавати словник
#     input_data = {
#         "messages": messages
#     }
#
#     response = agent.invoke(input_data)
#     # response -- словник з усією історією + відповідь моделі
#
#     # отримання всіє історії повідомлень
#     messages = response['messages']
#
#     # отримати фінальну відповідь моделі
#     answer = messages[-1]
#     print(answer.content)
#
#     # виведемння всієї історії
#     print()
#     print("Історія")
#
#     for message in messages:
#         print(repr(message))

# Завдання 3
# ===================================================================================================
# Напишіть модель яка конвертує одну валюту в іншу за нинішнім курсом.
# Для цього напишіть функції, яка отримує номінал та курс і робить конвертацію.
# Реалізуйте 2 ланцюга:
# перший отримує назви валют та шукає курс в інтернеті
# другий отримує номінал та курс і застосовує функцію ковертації

# Завдання 4
# ===================================================================================================
# Напишіть модель яка рекомендує міста для проведення вихідних.
# Користувач вводить назву країни та стиль відпочинку.
# Перший агент шукає популярні міста для відпочинку в потрібному стилі.
# Другий агент перевіряє погоду в цих містах та відсіює невдалі варіанти
# Третій агент виводить кожне місто що залишилось, та причину чому його варто відвідати(коротко)

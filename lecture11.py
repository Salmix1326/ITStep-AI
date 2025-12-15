# import os
# import dotenv
#
# from typing import List
# from pydantic import BaseModel, Field
# from langchain_google_genai import GoogleGenerativeAI
# from langchain.prompts import PromptTemplate
# from langchain.output_parsers import PydanticOutputParser
#
# # завантаження апі ключа
# dotenv.load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
#
# # створити llm
# llm = GoogleGenerativeAI(
#     model='gemini-2.5-flash',
#     api_key=api_key,
# )
#
#
# # Користувач задає питання.
# # Потрібно дати відповіть та запропопонувати цікаві факти по тій
# # же темі що і питання
#
# # # варіант 1 -- все в один промпт
# # prompt = PromptTemplate.from_template(
# #     """
# #     Ти -- чатбот для навчання. Твоя задача давати відповідь на питання.
# #     Також потрібно запропонувати декілька цікавих фактів по тій же темі
# #     що і питання
# #
# #     ### Питання
# #     {question}
# #     """
# # )
# #
# # chain1 = prompt | llm
# #
# # response = chain1.invoke({
# #     "question": "Коли була висадка на місяць"
# # })
# #
# # print(response)
#
#
# # варіант 2 -- розьити на 2 кроки
# # дати відповідь та визначити тему питання
# # згенерувати цікаві факти по темі
#
# # пишемо парсер
#
# # структура відповіді
# class ParserResult(BaseModel):
#     question_answer: str = Field(description="Answer to user question")
#     topics: List[str] = Field(description="список пов'язаних тем до питання")
#
#
# # створення парсера
# parser = PydanticOutputParser(pydantic_object=ParserResult)
#
# # інструкція для llm як має виглядати відповідь
# instructions = parser.get_format_instructions()
#
# prompt = PromptTemplate.from_template(
#     """
#     Ти -- чатбот для навчання. Твоя задача давати відповідь на питання.
#     Також потрібно визначити теми які відносяться до цього питання
#
#     ### Питання
#     {question}
#
#     ### ФОРМАТ ВІДПОВІДІ
#     {instructions}
#     """,
#     partial_variables={"instructions": instructions}  # одразу передаємо інструкції
# )
#
# chain = prompt | llm | parser
#
# question = input("Введіть питання: ")
#
# response = chain.invoke({
#     "question": question,
# })
#
# print(f"Відповідь: {response.question_answer}")
#
#
# # print(response)
# # print(type(response))
# #
# # print(response.question_answer)
# # print(response.topics)
#
# # генерація цікавих фактів на основі тем
# class FactResponse(BaseModel):
#     facts: List[str] = Field(description="список цікавих фактів розом з їхнім описом")
#
#
# # створення парсера
# parser = PydanticOutputParser(pydantic_object=FactResponse)
#
# # інструкція для llm як має виглядати відповідь
# instructions = parser.get_format_instructions()
#
# prompt = PromptTemplate.from_template(
#     """
#     Ти -- генератор цікавих фактів. Твоя задача навести 5 цікавих фактів
#     на задані теми
#
#     ### ТЕМИ
#     {topics}
#
#     ### ФОРМАТ ВІДПОВІДІ
#     {instructions}
#     """,
#     partial_variables={"instructions": instructions}  # одразу передаємо інструкції
# )
#
# chain2 = prompt | llm | parser
#
# response = chain2.invoke(
#     {
#         "topics": response.topics
#     }
# )
#
# facts = response.facts
#
# print("Цікаві факти")
# for fact in facts:
#     print(fact)
#
# whole_chain = chain | chain2

# Модуль 3. Generative AI, LLM
# Тема: Langchain. Частина 3
# Завдання 1
# Напишіть модель для рекомендації книг з двох ланцюгів:
# Перший ланцюг отримує назву книги та визначає її жанр
# Другий отримує назву книги, жанр та повертає список схожих книг(того ж самого жанру та іншого)
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
import dotenv
import os

from typing_extensions import List

# # завантажити api ключі з папки .env
# dotenv.load_dotenv()
#
# # отримати сам ключ
# api_key = os.getenv('GEMINI_API_KEY')
#
# # створити llm
# llm = GoogleGenerativeAI(
#     model='gemini-2.5-flash-lite',  # назва моделі
#     api_key=api_key,  # ваша API
# )

# # структура відповіді
# class ParserResult(BaseModel):
#     book_name: str = Field(description="Здесь пиши название книги")
#     genre: str = Field(description="Здесь пиши жанр книги")
#
# # # створення парсера
# parser = PydanticOutputParser(pydantic_object=ParserResult)
# instructions = parser.get_format_instructions()
#
# # промпт
# prompt = PromptTemplate.from_template(
#     """
#     Ты - знаток книг. К тебе будут обращаться люди с описанием книг. Определи жанр этой книги.
#
#     #Сообщение от пользователя
#     {question}
#
#     #ФОРМАТ ОТВЕТА
#     {instructions}
#     """
# )
#
# chain = prompt | llm | parser
#
# question = input("Опишите книгу: ")
#
# response = chain.invoke(
#     {
#         "question": question,
#         "instructions": instructions,
#     }
# )
#
# # промпт 2
# prompt = PromptTemplate.from_template(
#     """
#     Ты - знаток книг. Тебе надо порекомендовать книги человеку по названию и жанру книг.
#
#     #НАЗВАНИЕ КНИГИ
#     {book_name}
#
#     #ЖАНР
#     {genre}
#     """
# )
#
# chain2 = prompt | llm
#
# response = chain2.invoke(
#     {
#         "book_name": response.book_name,
#         "genre": response.genre,
#     }
# )
#
# print(response)

# Завдання 2
# Напишіть модель для генерації листа:
# Перший ланцюг отримує короткий опис листа та генерує основний зміст
# Другий ланцюг отримує основний зміст та стиль листа(формальний, неформальний, тощо) та генерує лист

# завантажити api ключі з папки .env
dotenv.load_dotenv()

# отримати сам ключ
api_key = os.getenv('GEMINI_API_KEY')

# створити llm
llm = GoogleGenerativeAI(
    model='gemini-2.5-flash-lite',  # назва моделі
    api_key=api_key,  # ваша API
)

def get_content_chain():
    # структура відповіді
    class ParserResult(BaseModel):
        content: str = Field(description="Здесь текст сообщения по данным")

    # # створення парсера
    parser = PydanticOutputParser(pydantic_object=ParserResult)
    instructions = parser.get_format_instructions()

    # промпт
    prompt = PromptTemplate.from_template(
        """
        Ты - помощник по составлению писем. Тебе нужно составить текст по описанию, которое напишет пользователь
        
        #Сообщение от пользователя
        {user_text}
        
        #ИНСТРУКЦИИ
        {instructions}
        
        """,
        partial_variables={"instructions": instructions}
    )

    chain = prompt | llm | parser

    return chain


def get_letter_chain():
    # промпт
    prompt = PromptTemplate.from_template(
        """
        Ты - помощник по составлению писем. Тебе нужно изменить содержание сообщения под стиль
        
        #СТИЛЬ СООБЩЕНИЯ
        {user_style}
        
        #СОДЕРЖАНИЕ
        {content}
        """
    )

    chain = prompt | llm

    return chain


user_text = input("Опишите содержание: ")
user_style = input("Опишите cтиль содержания: ")

content_chain = get_content_chain()

content_response = content_chain.invoke({
    "user_text": user_text
})

letter_chain = get_letter_chain()

letter_response = letter_chain.invoke({
    "user_style": user_style,
    "content": content_response.content
})

print(letter_response)




# Завдання 3
# Напишіть модель для генерації резюме:
# Перший ланцюг отримує опис вакансії та повертає основні навички, які необхідні
# Другий ланцюг отримує основні навички та опис кандидата і генерує резюме

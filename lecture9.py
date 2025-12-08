# LLM (Large Language Model)
# load API KEY as environment variable
import os
import dotenv


dotenv.load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

# connect to model

import langchain
from langchain_google_genai import GoogleGenerativeAI
# #
# # # create a model
# llm = GoogleGenerativeAI(
#     model='gemini-2.5-flash-lite', # model name
#     api_key=api_key,
#     top_k=10, # choose random next word from 10 with greater probability
#     top_p=0.8, # leave words, which probability sum not greater 80% and choose avg
#     temperature=1.2, # the higher the temperature - the more similar the percentages become
# )
# #
# # # start model
# # response = llm.invoke('Hi, what is LLM?')
# # print(response)

# request: Hi, what is LLM?

# part of response: LLM stands for **Large Language Model**.

# model task -- generate next word
# Probability generates for each word
# stands - 30%
# for = 25%
# apple - 0.000000%


# parameters of creativity
# temperature
# 0 - 0.3 -- low creativity (answers according to the manual)
# 0.7 - 1.2 -- average creativity (answers like a human)
# 1.5 - 1.7 -- high creativity (will come up with something interesting or lie)
# >2 -- random words


# Модуль 3. Generative AI, LLM
# Тема: Langchain. Частина 1
# Завдання 1
# ======================================================================================
# Підключіть модель LLM за допомогою свого API key. Попросіть модель згенерувати:
# ● коротку історію
# Підберіть параметри креативності та довжини

# # create a model
llm = GoogleGenerativeAI(
    model='gemini-2.5-flash-lite', # model name
    api_key=api_key,
    top_k=1, # choose random next word from 10 with greater probability
    top_p=0.8, # leave words, which probability sum not greater 80% and choose avg
    temperature=2, # the higher the temperature - the more similar the percentages become
)

# start model
# ● відповідь на питання у вигляді одного слова(наприклад яка столиця Франції?)
# response = llm.invoke('Give response with only one word. Tell me France capital name')

# ● код python
# response = llm.invoke('Give me Python code for sum 2 numbers, for example 3+2')

# ● коротку історію
# response = llm.invoke('Напиши историю о программисте, который попал в лес')
# print(response)

# Завдання 2
# Прочитайте файл data\lesson9\rules.txt з правилами користування атракціону.
# Напишіть програму яка отримує від користувачі питання та дає відповідь на нього виходячи з текстового файлу.
# Для цього об’єднайте правила користування з питанням користувача.
# Користувач задає питання поки не введе порожній рядок.
# Змініть файл rules.txt, щоб переконатись що модель дійсно його читає.

# with open('data/lesson9/rules.txt', 'r', encoding='utf-8') as file:
#     rules = file.read()
#
# user_question = input("enter question: ")
#
# response = llm.invoke(f'{rules} Вопрос: {user_question}. Дай ответ только по правилам. '
#                       f'Дай ответ тем же языком, на котором был задан вопрос')
# print(response)

# Завдання 3
# Створіть найпростіший чат бот. Напишіть моделі якого персонажа вона повинна вдавати(відомий актор, персонаж кіно\книги, тощо).
# Реалізуйте двома способами:
# 1. Модель отримує інструкцію в якому стилі відповідати та нове повідомлення.
# 2. Модель отримує інструкцію та історію попередніх повідомлень як від користувача, так і її власні відповіді у форматі
# Instruction: ….
# Human: massage1
# AI: message2
# Human: massage3
# AI: message4
# Human: massage5
# AI:
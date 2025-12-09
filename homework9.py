# Модуль 3. Generative AI, LLM
# Тема: Langchain. Частина 1
# Завдання 1
# ==========================================================================================================
# Прочитайте файл data\lesson9\return_policy.txt
# Та напишіть простий чат бот для відповідей на питання користувачів стосовно повернення товару.
# Діалог завершується коли користувач вводить порожній рядок.
# Передавайте усю історію спілкування у форматі:
# Instruction: ….
# Human: massage1
# AI: message2
# Human: massage3
# AI: message4
# Human: massage5
# AI:
import os
import dotenv
from langchain_google_genai import GoogleGenerativeAI


dotenv.load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

llm = GoogleGenerativeAI(
    model='gemini-2.5-flash-lite', # model name
    api_key=api_key,
    top_k=10, # choose random next word from 10 with greater probability
    top_p=0.8, # leave words, which probability sum not greater 80% and choose avg
    temperature=1.2, # the higher the temperature - the more similar the percentages become
)

with open('data/lesson9/return_policy.txt', 'r', encoding='utf-8') as file:
    policy = file.read()

chat_history = (f'Вот инструкции магазина по товару {policy}. Ты - констультант магазина и к тебе обращаются посетители.'
                f'Если посетитель задает уже второй вопрос - ненадо снова представляться кто ты.')

while True:
    user_question = input("Ваш вопрос: ")
    chat_history += f'Вопрос посетителя: {user_question}'

    response = llm.invoke(f'{chat_history}')
    model_response = f"Твой ответ: {response}"
    chat_history += model_response

    print(f"Консультант: {response}")
    exit_program = input("Желаете продолжить консультацию? (y/n): ")

    if exit_program == "n":
        print("Выход из чата...")
        break

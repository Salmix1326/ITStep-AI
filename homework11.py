# Модуль 3. Generative AI, LLM
# Тема: Langchain. Частина 3
# Завдання 1
# ===========================================================================================
# Напишіть модель для генерації персонального плану тренувань з двох ланцюгів:
# Перший ланцюг отримує мету тренування(схуднення, набір м’язів, тощо) та повертає список вправ
# Другий ланцюг отримує список вправ, рівень підготовки користувача(низький, середній, професіонал)
# та кількість часу на тиждень(в годинах) і повертає план тренувань
from typing import List
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
import dotenv
import os


# завантажити api ключі з папки .env
dotenv.load_dotenv()

# отримати сам ключ
api_key = os.getenv('GEMINI_API_KEY')

# створити llm
llm = GoogleGenerativeAI(
    model='gemini-2.5-flash-lite',  # назва моделі
    api_key=api_key,  # ваша API
)


def get_exercises_chain():
    # структура відповіді
    class ParserResult(BaseModel):
        exercises: List[str] = Field(description="список упражнений для цели")

    # # створення парсера
    parser = PydanticOutputParser(pydantic_object=ParserResult)
    instructions = parser.get_format_instructions()

    # промпт для списка упражнений
    prompt = PromptTemplate.from_template(
        """
        Ты - помощник по составлению плана тренировок. Тебе нужно составить список упражнений по описанию, 
        которое напишет пользователь. Он будет описывать свою цель. Цели могут быть разные: похудение, 
        набор мышц и тд.

        #Сообщение от пользователя
        {user_sport_aim}

        #ИНСТРУКЦИИ
        {instructions}

        """,
        partial_variables={"instructions": instructions}
    )

    chain = prompt | llm | parser

    return chain


def get_gym_plan_chain():
    # промпт для плана
    prompt = PromptTemplate.from_template(
        """
        Ты - помощник по составлению тренировок. Тебе нужно составить план тренировок в зависимости от данных, которые 
        напишет пользователь. Он даст список упражнений, время и уровень подготовки. Ответ пиши строго по списку, который
        будет в наличии при запросе. По списку разбирай план каждого упражнения. Пытайся составить план, который отлично 
        подойдет для конкретного случая.
        
        #ПРИМЕРЫ ЗАПРОСОВ
        1. У меня 2 часа времени в неделю, я новичок
        2. Много свободного времени, уровень продвинутый
        3. Незнаю точно, как бы хотел заниматься
        
        #ЛОГИЧЕСКИЕ ШАГИ
        1. Изучить список тренировок, каждое упражнение
        2. Написать небольшое общее привестствие и далее по списку расписать каждое упражнение по отдельным абзацам
        3. В конце каждого абзаца указывать статистику упражнения, в виде: Время: Уровень: Целевые мыщцы: 
        Насколько полезно для сжигания каллорий или набора мышечной массы:
        4. Пытайся делать тренировки по дням в распределении общего плана на неделю. 
        Тренировка должна быть сбалансированной
        5. Не выходи за рамки времени пользователя. 
        Если есть конфликт времени пользователя с планом тренировок, 
        который у тебя получился - добаляй в план только самые нужные

        #ВРЕМЯ И УРОВЕНЬ ПОДГОТОВКИ ПОЛЬЗОВАТЕЛЯ
        {user_time_and_sport_level}

        #СПИСОК УПРАЖНЕНИЙ
        {exercises_response}
        """
    )

    chain = prompt | llm

    return chain


# данные пользователя
user_sport_aim = input("Опишите свою цель, для чего хотите заняться спортом: ")
user_time_and_sport_level = input("Укажите время и уровень подготовки: ")

# цепи для запроса нейросети

# для списка упражнений
exercises_chain = get_exercises_chain()

exercises_response = exercises_chain.invoke({
    "user_sport_aim": user_sport_aim
})

print(exercises_response.exercises)

# для плана тренировок
gym_plan_chain = get_gym_plan_chain()

gym_plan_response = gym_plan_chain.invoke({
    "user_time_and_sport_level": user_time_and_sport_level,
    "exercises_response": exercises_response.exercises
})

print(gym_plan_response)
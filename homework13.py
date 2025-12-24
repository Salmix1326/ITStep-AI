# Модуль 3. Generative AI, LLM
# Тема: Langchain. Частина 5
# Завдання 1
# ==================================================================================================
# Напишіть чат бота, з інструментом по рекомендації ресторанів.
# Для цього скористайтесь GoogleSerperAPIWrapper(type="places")
# Інструмент повинен отримувати запит для пошуку та повертати таку інформацію про ресторани:
# назва
# посилання на сайт(якщо є)
# рейтинг
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

# інструмент для пошуку в інтернеті
searcher = GoogleSerperAPIWrapper(serper_api_key=serper_api_key, type="places")

# функция для поиска мест и сбора данных
def get_places_info(query: str) -> list:
    """
    Function for search information about some places
    Function returns place info in dictionary
    :param query:
    :return:
    """
    search_info = searcher.results(query)
    search_places_info = search_info["places"]
    result_list = []

    for search_place in search_places_info:
        result_place_info = {}

        if "title" in search_place:
            result_place_info["title"] = search_place["title"]

        if "website" in search_place:
            result_place_info["website"] = search_place["website"]

        if "rating" in search_place:
            result_place_info["rating"] = search_place["rating"]

        result_list.append(result_place_info)

    return result_list


# створення агента
agent = create_react_agent(
    model=llm,  # мовна модель
    tools=[get_places_info]
)

# історія повідомлень + інструкції
messages = [
    SystemMessage(
        """
        Ты - консультант по местам в мире.
        Пользователи будут спрашивать о разных местах.
        Тебе нужно рассказывать и рекомендовать места вместе со статистикой о них.
        Для этого у тебя есть инструменты для поиска мест и сбора информации о них.
        Строго запрашивай данные из интструментов.
        Если нужных данных данных не будет - добавь немного своих.
        Описывай места красочно и со вкусом.
        Зачастую может быть сбой в запросе query у функции.
        Поэтому переводи их запрос на английский перед использованием функции.
        Если не пришли данные - уточни какие конкретно места интересуют пользователя.
        Будь то отели/места для отдыха и так далее.
        Запрос на функцию делай с как можно большим количеством слов

        #ИНСТРУМЕНТЫ
        * get_place_info
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
    # print()
    # print("Історія")
    #
    # for message in messages:
    #     print(repr(message))

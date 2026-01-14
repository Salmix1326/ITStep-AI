# Модуль 3. Generative AI, LLM
# Тема: Langchain. Частина 7
# Завдання 1
# ==============================================================================
# Напишіть додаток з чат ботом по допомозі з вивченням англійської мови.
# Якщо користувач просить перекласти слово або фразу, то вивести переклад та приклад використання у речені
# Якщо користувач просить перекласти речення, то вивести переклад та пояснення граматики,
# наприклад структура there is/are, пасивна форма дієслова, тощо
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
)

# заголовок
st.title("English Language Teacher Chat Bot")

# завантаження апі ключа за допомогою streamlit
api_key = st.secrets.get("GEMINI_API_KEY")

# створити llm
llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash-lite',
    api_key=api_key,
)

# запрос пользователя
user_query = st.chat_input("Ваше повідомлення")

# якщо це початок то створити історію в session state
if user_query is None:
    # історія повідомлень
    st.session_state['history'] = [
        # перше повідомлення з основними інструкціями(промпт)
        SystemMessage(
            """
            Ти -- ввічливий чат бот по допомозі з вивченням англійської мови.
            Якщо користувач просить перекласти слово або фразу, то вивести переклад та приклад використання у речені
            Якщо користувач просить перекласти речення, то вивести переклад та пояснення граматики
            
            # ПРИКЛАДИ
            Структура there is/are, пасивна форма дієслова, тощо
            Рiзнi речення про правила використування do/to be/passive verbs
            Чiтке пояснення речення, якщо для людини ця тема нова
            """
        )
    ]

# якщо повідомлення введено, то дати відповідь від моделі
if user_query:
    # переволимо повідомлення в HumanMessage
    human_message = HumanMessage(user_query)

    # добавляємо до історії повідомлень
    st.session_state['history'].append(human_message)

    # запускаємо модель
    response = llm.invoke(st.session_state['history'])

    # response -- AIMessage
    # добавляємо до історії повідомлень
    st.session_state['history'].append(response)

# вывод всей истории общения
for message in st.session_state['history']:
    if isinstance(message, SystemMessage):
        continue

    # содержание сообщения
    text = message.content

    # получить роль
    if isinstance(message, HumanMessage):
        role = "human"

    else:
        role = "ai"

    with st.chat_message(role):
        st.markdown(text)

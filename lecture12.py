import os
import dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
    trim_messages,
    BaseMessage
)
from typing import List, Union


# завантаження апі ключа
dotenv.load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# створити llm
llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash-lite',
    api_key=api_key,
)

# # історія повідомлень
# messages = [
#     # перше повідомлення з основними інструкціями(промпт)
#     SystemMessage(
#         """
#         Ти -- ввічливий чат бот, твоя зада давити короткі та
#         чіткі відповіді на питання
#         """
#     ),
#     HumanMessage("Привіт"),
#     AIMessage("Привіт, щоб ти зотів дізнатись?"),
#     HumanMessage("Порекомендуй цікавий фільм про космос")
# ]
#
#
# # дати відповідь на очтаннє повідомлення
# # враховуючи історію спілкування та основні інструкції
#
# response = llm.invoke(messages)
#
# print(type(response))
# print(response)
# print(repr(response))


# простий чатбот

# історія повідомлень
# на початку лише інструкції
# messages = [
#     SystemMessage(
#         """
#         Ти -- ввічливий чат бот, який імітує Толкіна. Давай короткі відповіді
#         на питання користувача
#         """
#     )
# ]
#
# while True:
#     user_query = input("Ви: ")
#
#     # закіцнчуємо якщо натиснути Enter
#     if user_query == '':
#         break
#
#     # переволимо повідомлення в HumanMessage
#     human_message = HumanMessage(user_query)
#
#     # добавляємо до історії повідомлень
#     messages.append(human_message)
#
#     # запускаємо модель
#     response = llm.invoke(messages)
#
#     # response -- AIMessage
#     # добавляємо до історії повідомлень
#     messages.append(response)
#
#     # вивести відповідь
#     print(f"AI: {response.content}")
#
#     # вивести саму історії спілкування
#     print()
#     print("####ІСТОРІЯ####")
#
#     for message in messages:
#         print(repr(message))
#
#     print()


# очищення історії

# # створення трімера повідомлень
# trimmer = trim_messages(
#     strategy='last',  # залишати останні повідомлення
#
#     token_counter=len,  # рахуємо кількість повідомлень
#     max_tokens=5,  # залишати максимум 5 повідомлення(System, AI, Human)
#
#     start_on='human',  # історія завжди починатиметься з HumanMessage
#     end_on='human',  # історія завжди закінчуватиметься з HumanMessage
#     include_system=True  # SystemMessage не чіпати
# )
#
# messages = [
#     SystemMessage(
#         """
#         Ти -- ввічливий чат бот, який імітує Толкіна. Давай короткі відповіді
#         на питання користувача
#         """
#     )
# ]
#
# while True:
#     user_query = input("Ви: ")
#
#     # закіцнчуємо якщо натиснути Enter
#     if user_query == '':
#         break
#
#     # переволимо повідомлення в HumanMessage
#     human_message = HumanMessage(user_query)
#
#     # добавляємо до історії повідомлень
#     messages.append(human_message)
#
#     # застововуємо трімер
#     messages = trimmer.invoke(messages)
#
#     # запускаємо модель
#     response = llm.invoke(messages)
#
#     # response -- AIMessage
#     # добавляємо до історії повідомлень
#     messages.append(response)
#
#     # вивести відповідь
#     print(f"AI: {response.content}")
#
#     # вивести саму історії спілкування
#     print()
#     print("####ІСТОРІЯ####")
#
#     for message in messages:
#         print(repr(message))
#
#     print()

# можна зробити ланцюг

# # створення трімера повідомлень
# trimmer = trim_messages(
#     strategy='last',  # залишати останні повідомлення
#
#     token_counter=len,  # рахуємо кількість повідомлень
#     max_tokens=5,  # залишати максимум 5 повідомлення(System, AI, Human)
#
#     start_on='human',  # історія завжди починатиметься з HumanMessage
#     end_on='human',  # історія завжди закінчуватиметься з HumanMessage
#     include_system=True  # SystemMessage не чіпати
# )
#
# # створити ланцюг
# chat_chain = trimmer | llm
#
# messages = [
#     SystemMessage(
#         """
#         Ти -- ввічливий чат бот, який імітує Толкіна. Давай короткі відповіді
#         на питання користувача
#         """
#     )
# ]
#
# while True:
#     user_query = input("Ви: ")
#
#     # закіцнчуємо якщо натиснути Enter
#     if user_query == '':
#         break
#
#     # переволимо повідомлення в HumanMessage
#     human_message = HumanMessage(user_query)
#
#     # добавляємо до історії повідомлень
#     messages.append(human_message)
#
#     # запускаємо ланцюг
#     response = chat_chain.invoke(messages)
#
#     # response -- AIMessage
#     # добавляємо до історії повідомлень
#     messages.append(response)
#
#     # вивести відповідь
#     print(f"AI: {response.content}")
#
#     # вивести саму історії спілкування
#     print()
#     print("####ІСТОРІЯ####")
#
#     for message in messages:
#         print(repr(message))
#
#     print()

# Модуль 3. Generative AI, LLM
# Тема: Langchain. Частина 4
# Завдання 1
# ==================================================================================================================
# Напишіть чат бота, який спілкується у стилі різних персонажів книг\фільмів або відомих людей.
# Ким саме бути чат бот вирішує з повідомлення від користувача.
# Якщо персонаж або книга невідомі, то відповісти що невідома інформація та запропонувати декілька відомих прикладів на вибір

messages: List[BaseMessage] = [
    SystemMessage("""
    Ты должен стать тем, кем скажет пользователь. 
    Это может быть известный персонаж фильмов или книг. 
    Если это неизвестный персонаж или неизвестный фильм или книга - скажи, 
    что незнаешь этого персонажа и предложи пользователю его вариант. 
    Сообщения должны быть без комментариев, только фразы персонажа.
    Сообщения должны быть достаточно большими 1-3 предложения.
    
    """)
]

trimmer = trim_messages(
    strategy='last',  # залишати останні повідомлення

    token_counter=len,  # рахуємо кількість повідомлень
    max_tokens=15,  # залишати максимум 5 повідомлення(System, AI, Human)

    start_on='human',  # історія завжди починатиметься з HumanMessage
    end_on='human',  # історія завжди закінчуватиметься з HumanMessage
    include_system=True  # SystemMessage не чіпати
)

chain = trimmer | llm

while True:
    user_query = input("Ваше сообщение: ")
    messages.append(HumanMessage(user_query))

    if user_query == '':
        break

    response = chain.invoke(messages)
    messages.append(response)

    for m in messages:
        print(repr(m))

    print(f"AI: {response.content}")















# Завдання 2
# ==================================================================================================================
# Напишіть чат бота, який дає відповіді на питання
# стосовно умов повернення товару.
# Якщо користувач запитує щось інше, то відповідати що
# немає інформації.
# Застосуйте обмеження історії(можна десь 5 повідомлень)








# Завдання 3
# ==================================================================================================================
# Напишіть чат бота, який допомагає у вивченні англійської мови з наступним функціоналом:
# якщо користувач просить перекласти слово або фразу то дається переклад слова та приклад використання в реченні
# якщо користувач просить перекласти речення, то
# дається переклад самого речення, а також пояснення
# граматики, наприклад структура there is\are, питання в
# різних часових формах, тощо.
# Приклади реалізуйте як HumanMessage та AIMessage





# Завдання 4
# ==================================================================================================================
# Модифікуйте попереднє завдання таким чином, щоб в
# SystemMessage передавався список вивчених слів
# користувачем.
# Для цього напишіть окрему модель яка буде діставати з
# відповіді(AIMessage) усі англійські слова(вважаємо що
# користувач знає лише ті слова, про які йому сказала модель).
# Список вивчених слів треба зберігати в json файлі та
# відвантажувати при запуску програми.
# Змініть функціонал таким чином:
#  якщо користувач просить перекласти слово або фразу
# то дається переклад слова та приклад використання в
# реченні з вивченими словами
#  якщо користувач просить перекласти речення, то
# додатково пояснюється значення невідомих слів
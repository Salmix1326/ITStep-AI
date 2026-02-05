import cv2
import mediapipe as mp
import math
import time
import win32com.client

# выбор классов для распознавания рук
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# использование своей камеры
cap = cv2.VideoCapture(0)

# начальные настройки для таймера на удержание жестов
gesture_start_time = None  # когда жест впервые появился
required_hold = 1  # удерживать 2 секунды

# Робота с PowerPoint -------------------------------------------------------------------------
# объект PowerPoint
ppt = win32com.client.Dispatch("PowerPoint.Application")
ppt.Visible = True # окно PowerPoint
prs = ppt.Presentations.Open(r"C:\users\shapa\downloads\example.pptx")
window = prs.Windows(1) # текущее окно презентации

# функции для листания слайдов
def go_next_slide():
    current_slide = window.View.Slide.SlideIndex
    if current_slide < prs.Slides.Count:
        window.View.GotoSlide(current_slide + 1)


def go_prev_slide():
    current_slide = window.View.Slide.SlideIndex
    if current_slide > 1:
        window.View.GotoSlide(current_slide - 1)


# подключение модели для распознавания рук
with mp_hands.Hands(
    static_image_mode=False, # модель отслеживает руки между кадрами
    max_num_hands=2,
    model_complexity=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as hands:

# основной цикл работы для камеры
    while True:
        success, frame = cap.read()
        if not success:
            break

        # изменение параметров видео
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # результат работы модели
        results = hands.process(rgb)

        # отрисовка точек рук
        if results.multi_hand_landmarks: # список из рук
            # размеры окна видео
            h, w, _ = frame.shape

            for hand_landmarks, hand_label_info in zip(results.multi_hand_landmarks, results.multi_handedness): # для каждой руки
                mp_draw.draw_landmarks(
                    frame, # кадр
                    hand_landmarks, # одна из рук
                    mp_hands.HAND_CONNECTIONS # связи между 21 точками
                )

                # проверка на правильность руки
                hand_label = hand_label_info.classification[0].label

                if hand_label == "Right":
                    continue

                # проверки на положение пальцев
                # большой палец ---------------------------------------
                # кончик и сустав большого пальца
                thumb_tip = hand_landmarks.landmark[4]
                thumb_mcp = hand_landmarks.landmark[2]

                # остальные пальцы ------------------------------------
                # кончик и суставы указательного пальца
                index_tip = hand_landmarks.landmark[8]
                index_dip = hand_landmarks.landmark[7]
                index_pip = hand_landmarks.landmark[6]
                index_mcp = hand_landmarks.landmark[5]

                # кончик суставы среднего пальца
                middle_tip = hand_landmarks.landmark[12]
                middle_dip = hand_landmarks.landmark[11]
                middle_pip = hand_landmarks.landmark[10]
                middle_mcp = hand_landmarks.landmark[9]

                # кончик суставы безымянного пальца
                ring_tip = hand_landmarks.landmark[16]
                ring_dip = hand_landmarks.landmark[15]
                ring_pip = hand_landmarks.landmark[14]
                ring_mcp = hand_landmarks.landmark[13]

                # кончик суставы мизинца
                pinky_tip = hand_landmarks.landmark[20]
                pinky_dip = hand_landmarks.landmark[19]
                pinky_pip = hand_landmarks.landmark[18]
                pinky_mcp = hand_landmarks.landmark[17]

                # условия положения руки ----------------------------------------------------------------
                # условие на сгиб четырех пальцев кроме большого
                fingers_folded_for_left = (
                        index_tip.y > index_mcp.y and
                        middle_tip.y > middle_mcp.y and
                        ring_tip.y > ring_mcp.y and
                        pinky_tip.y > pinky_mcp.y
                )

                fingers_folded_for_right = (
                        index_tip.y < index_mcp.y and
                        middle_tip.y < middle_mcp.y and
                        ring_tip.y < ring_mcp.y and
                        pinky_tip.y < pinky_mcp.y
                )

                # условие на глубину положения пальцев относительно камеры ------------------------------------
                # средняя глубина от камеры для пальцев
                avg_z = (index_tip.z + middle_tip.z + ring_tip.z + pinky_tip.z + thumb_tip.z) / 5
                threshold = 0.02  # общее значение равности друг от друга по глубине

                fingers_aligned = (
                        abs(thumb_tip.z - avg_z) < threshold and
                        abs(index_tip.z - avg_z) < threshold and
                        abs(middle_tip.z - avg_z) < threshold and
                        abs(ring_tip.z - avg_z) < threshold and
                        abs(pinky_tip.z - avg_z) < threshold
                )

                # условие угол фаланг пальцев ----------------------------------------------------------------
                # вычисление угла для согнутости пальцев
                def angle(a, b, c):
                    """Возвращает угол в градусах между точками a-b-c"""
                    ab = (b.x - a.x, b.y - a.y, b.z - a.z)
                    cb = (b.x - c.x, b.y - c.y, b.z - c.z)
                    dot = sum(ab[i] * cb[i] for i in range(3))
                    mag_ab = math.sqrt(sum(x * x for x in ab))
                    mag_cb = math.sqrt(sum(x * x for x in cb))
                    return math.degrees(math.acos(dot / (mag_ab * mag_cb)))


                angle_index_finger = angle(index_dip, index_pip, index_mcp)
                angle_middle_finger = angle(middle_dip, middle_pip, middle_mcp)
                angle_ring_finger = angle(ring_dip, ring_pip, ring_mcp)
                angle_pinky_finger = angle(pinky_dip, pinky_pip, pinky_mcp)
                threshold_angle = 70

                fingers_target_angle = (
                        angle_index_finger < threshold_angle and
                        angle_middle_finger < threshold_angle and
                        angle_ring_finger < threshold_angle and
                        angle_pinky_finger < threshold_angle
                )

                # условие на положение большого пальца по фалангам - влево/вправо + проверка на выпрямление
                is_thumb_extended_left = thumb_tip.x > thumb_mcp.x and (thumb_tip.x - thumb_mcp.x) > 0.05  # влево
                is_thumb_extended_right = thumb_tip.x < thumb_mcp.x and (
                        thumb_tip.x - thumb_mcp.x) < -0.05  # вправо

                # условие большого пальца в сторону от других пальцев
                thumb_on_side_left = thumb_tip.x > pinky_mcp.x and thumb_tip.x > index_mcp.x  # влево
                thumb_on_side_right = thumb_tip.x < pinky_mcp.x and thumb_tip.x < index_mcp.x  # вправо

                # общая совокупность проверок для жестов
                is_gesture_left = (
                    fingers_folded_for_left and
                    fingers_aligned and
                    is_thumb_extended_left and
                    thumb_on_side_left and
                    fingers_target_angle
                )

                is_gesture_right = (
                        fingers_folded_for_right and
                        fingers_aligned and
                        is_thumb_extended_right and
                        thumb_on_side_right and
                        fingers_target_angle
                )

                # условия на жест для написания текста -----------------------------------------------------
                # большой палец вверх
                thumb_up = (thumb_tip.y - thumb_mcp.y) < -0.12

                # таймер на удержание жестов
                current_time = time.time() # текущее время

                # удержание жеста
                if is_gesture_left or is_gesture_right or (thumb_up and fingers_target_angle):
                    if gesture_start_time is None:
                        gesture_start_time = current_time  # начинаем отсчёт
                    elif (current_time - gesture_start_time) >= required_hold:
                        if is_gesture_left:
                            go_prev_slide()
                            print("Thumb gesture left")

                        elif is_gesture_right:
                            go_next_slide()
                            print("Thumb gesture right")

                        else:
                            current_slide = window.View.Slide
                            current_slide.Shapes.Title.TextFrame.TextRange.Text = "Магия! Здесь появился текст!!!"
                            current_slide.Shapes.Placeholders(2).TextFrame.TextRange.Text = "Новый текст на активном слайде"
                            prs.Save()
                            print("Thumb gesture up")

                        gesture_start_time = None  # сброс таймера
                else:
                    gesture_start_time = None  # жест пропал, сброс отсчёта

                # показ координат точек руки
                # for idx, lm in enumerate(hand_landmarks.landmark):
                #     cx = int(lm.x * w)  # x в пикселях
                #     cy = int(lm.y * h)  # y в пикселях
                #
                #     # маленький кружок
                #     cv2.circle(frame, (cx, cy), 3, (0, 255, 0), -1)
                #
                #     # номера точек и пиксельные координаты
                #     cv2.putText(
                #         frame,
                #         f"{idx} ({cx},{cy})",
                #         (cx + 5, cy - 5),
                #         cv2.FONT_HERSHEY_SIMPLEX,
                #         0.4,
                #         (0, 255, 0),
                #         1
                #     )

        # показ видео с точками
        cv2.imshow("img", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# закрытие видео и презентации
cap.release()
prs.Close()
ppt.Quit()
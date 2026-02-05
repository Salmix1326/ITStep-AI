import cv2
import mediapipe as mp
import math
import time
import win32com.client

# Настройка MediaPipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# Таймер удержания жестов
gesture_start_time = None
required_hold = 1  # время удержания в секундах

# PowerPoint
ppt = win32com.client.Dispatch("PowerPoint.Application")
ppt.Visible = True
prs = ppt.Presentations.Open(r"C:\users\shapa\downloads\example.pptx")
window = prs.Windows(1)

# Функции для перелистывания слайдов
def go_next_slide():
    current_slide = window.View.Slide.SlideIndex
    if current_slide < prs.Slides.Count:
        window.View.GotoSlide(current_slide + 1)

def go_prev_slide():
    current_slide = window.View.Slide.SlideIndex
    if current_slide > 1:
        window.View.GotoSlide(current_slide - 1)

# Вспомогательная функция
def angle(a, b, c):
    """Возвращает угол в градусах между точками a-b-c"""
    ab = (b.x - a.x, b.y - a.y, b.z - a.z)
    cb = (b.x - c.x, b.y - c.y, b.z - c.z)
    dot = sum(ab[i] * cb[i] for i in range(3))
    mag_ab = math.sqrt(sum(x * x for x in ab))
    mag_cb = math.sqrt(sum(x * x for x in cb))
    if mag_ab * mag_cb == 0:
        return 180  # защита от деления на ноль
    return math.degrees(math.acos(dot / (mag_ab * mag_cb)))

# ---------------------- Основной цикл ----------------------
with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    model_complexity=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as hands:

    while True:
        success, frame = cap.read()
        if not success:
            break

        # обработка видео
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            h, w, _ = frame.shape

            for hand_landmarks, hand_label_info in zip(results.multi_hand_landmarks, results.multi_handedness):
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS) # для каждой руки

                hand_label = hand_label_info.classification[0].label
                if hand_label == "Right": # анализируем правую руку относительно камеры
                    continue

                # ---------------------- Координаты пальцев ----------------------
                # Больной палец и фаланги
                thumb_tip = hand_landmarks.landmark[4]
                thumb_mcp = hand_landmarks.landmark[2]

                # Указательный палец и фаланги
                index_tip = hand_landmarks.landmark[8]
                index_mcp = hand_landmarks.landmark[5]
                index_pip = hand_landmarks.landmark[6]
                index_dip = hand_landmarks.landmark[7]

                # Средний палец и фаланги
                middle_tip = hand_landmarks.landmark[12]
                middle_mcp = hand_landmarks.landmark[9]
                middle_pip = hand_landmarks.landmark[10]
                middle_dip = hand_landmarks.landmark[11]

                # Безымянный палец и фаланги
                ring_tip = hand_landmarks.landmark[16]
                ring_mcp = hand_landmarks.landmark[13]
                ring_pip = hand_landmarks.landmark[14]
                ring_dip = hand_landmarks.landmark[15]

                # Мизинец и фаланги
                pinky_tip = hand_landmarks.landmark[20]
                pinky_mcp = hand_landmarks.landmark[17]
                pinky_pip = hand_landmarks.landmark[18]
                pinky_dip = hand_landmarks.landmark[19]

                # ---------------------- Проверки жестов ----------------------
                # Сгиб остальных пальцев
                fingers_folded_for_left = (
                    index_tip.y > index_mcp.y + 0.01 and
                    middle_tip.y > middle_mcp.y + 0.01 and
                    ring_tip.y > ring_mcp.y + 0.01 and
                    pinky_tip.y > pinky_mcp.y + 0.01
                )

                fingers_folded_for_right = (
                    index_tip.y < index_mcp.y - 0.01 and
                    middle_tip.y < middle_mcp.y - 0.01 and
                    ring_tip.y < ring_mcp.y - 0.01 and
                    pinky_tip.y < pinky_mcp.y - 0.01
                )

                # Проверка глубины пальцев
                avg_z = (index_tip.z + middle_tip.z + ring_tip.z + pinky_tip.z + thumb_tip.z) / 5
                threshold_z = 0.03
                fingers_aligned = all(abs(lm.z - avg_z) < threshold_z for lm in [thumb_tip, index_tip, middle_tip, ring_tip, pinky_tip])

                # Углы фаланг
                threshold_angle = 75
                fingers_target_angle = (
                    angle(index_dip, index_pip, index_mcp) < threshold_angle and
                    angle(middle_dip, middle_pip, middle_mcp) < threshold_angle and
                    angle(ring_dip, ring_pip, ring_mcp) < threshold_angle and
                    angle(pinky_dip, pinky_pip, pinky_mcp) < threshold_angle
                )

                # Большой палец в выпрямлен
                is_thumb_extended_left = thumb_tip.x - thumb_mcp.x > 0.03
                is_thumb_extended_right = thumb_tip.x - thumb_mcp.x < -0.03

                # Большой палец в сторону
                thumb_on_side_left = thumb_tip.x > max(index_mcp.x, pinky_mcp.x)
                thumb_on_side_right = thumb_tip.x < min(index_mcp.x, pinky_mcp.x)

                # Большой палец вверх
                thumb_up = (thumb_tip.y - thumb_mcp.y) < -0.1

                # Проверка на выполнение жестов
                is_gesture_left = fingers_folded_for_left and fingers_aligned and is_thumb_extended_left and thumb_on_side_left and fingers_target_angle
                is_gesture_right = fingers_folded_for_right and fingers_aligned and is_thumb_extended_right and thumb_on_side_right and fingers_target_angle

                # ---------------------- Таймер удержания ----------------------
                current_time = time.time()

                if is_gesture_left or is_gesture_right or (thumb_up and fingers_target_angle):
                    if gesture_start_time is None:
                        gesture_start_time = current_time
                    elif (current_time - gesture_start_time) >= required_hold:
                        if is_gesture_left:
                            go_prev_slide()
                            print("Gesture Left")

                        elif is_gesture_right:
                            go_next_slide()
                            print("Gesture Right")

                        else:  # большой палец вверх
                            current_slide = window.View.Slide
                            current_slide.Shapes.Title.TextFrame.TextRange.Text = "Магия! Здесь появился текст!!!"
                            current_slide.Shapes.Placeholders(2).TextFrame.TextRange.Text = "Новый текст на активном слайде"
                            prs.Save()
                            print("Gesture Thumb Up")

                        gesture_start_time = None  # сброс таймера
                else:
                    gesture_start_time = None

        cv2.imshow("img", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Закрытие
cap.release()
prs.Close()
ppt.Quit()

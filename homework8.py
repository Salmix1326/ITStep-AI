# Модуль 2. Комп’ютерний зір
# Тема: opencv. Частина 2
# Завдання 1
# =================================================================================================
# Відкрийте відео data/lesson_pose/squat.mp4
# Ваша задача рахувати кількість присідань.
# Отримайте перший кадр та виділіть основні точки.
# Отримайте координати 3-ох точок ноги
# Визначте кут між цими трьома точками.
# Скористайтесь функцією utils.get_angle(x1, y1, x2, y2, x3, y3) де x2, y2 – координати коліна(центральна точка)
# Запустіть відео та добавте на сам кадр кут згинання ніг.
# Визначіть нижню межу кута(якщо людина опустилась нижче вважаємо що вона достатньо опустилась) та верхню
# межу кута(якщо людина піднялась вище вважаємо що вона достатньо піднялась)
# Добавте кількість присідань та кут на кожен кадр.
import cv2
import ultralytics
import numpy as np


# функция для угла
def get_angle(x1, y1, x2, y2, x3, y3):
    a = np.array([x1, y1])
    b = np.array([x2, y2])
    c = np.array([x3, y3])

    ab = a - b
    cb = c - b

    dot = ab @ cb
    norm_ab = (ab @ ab) ** 0.5
    norm_cb = (cb @ cb) ** 0.5
    angle = np.arccos(dot / norm_ab / norm_cb)
    angle = angle / np.pi * 180

    return angle


# видео и переменные
orig_video = cv2.VideoCapture('data/lesson_pose/squat.mp4')
model = ultralytics.YOLO('yolo11s-pose.pt')
move_down = True
squat_counter = 0

while True:
    success, img = orig_video.read()

    if not success:
        break

    # работа с model
    img_resized = cv2.resize(img, None, fx=0.5, fy=0.5)
    model_results = model.predict(img_resized)
    model_result = model_results[0]
    img_with_plot = model_result.plot()

    # получение keypoints
    keypoints = model_result.keypoints
    xy = keypoints.xy

    # получение координат
    right_foot_upper = xy[0,12]
    x_right_foot_upper = right_foot_upper[0]
    y_right_foot_upper = right_foot_upper[1]

    right_foot_center = xy[0, 14]
    x_right_foot_center = right_foot_center[0]
    y_right_foot_center = right_foot_center[1]

    right_foot_down = xy[0, 16]
    x_right_foot_down = right_foot_down[0]
    y_right_foot_down = right_foot_down[1]

    # получение угла
    foot_angle = get_angle(x_right_foot_upper, y_right_foot_upper,
                           x_right_foot_center, y_right_foot_center, x_right_foot_down, y_right_foot_down)

    # определение приседаний - человек присел
    if foot_angle < 70 and move_down:
        squat_counter += 1
        move_down = False

    # человек встал
    if foot_angle > 160 and not move_down:
        move_down = True

    print(foot_angle)
    cv2.putText(
        img_with_plot,                  # зображення
        f'Squats counter: {squat_counter}',    # текст
        (20, 20),     # верхний левый угол
        cv2.FONT_HERSHEY_SIMPLEX,    # шрифт
        0.8,          # розмір шрифту(відсоток до стандарту)
        (255, 255, 255),      # колір у bgr(тут чорний)
        2           # товщина ліній

    )

    cv2.imshow("img_with_plot", img_with_plot)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

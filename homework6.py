# Завдання 1
# =================================================================================================
# Відкрийте відео з файлу data\lesson8\meetings.mp4
# Застосуйте детекцію та виведіть результат, підберіть параметри
# Можете змінити розмір кадру для кращої візуалізації cv2.resize()
import cv2
import ultralytics

model = ultralytics.YOLO('yolov8s.pt')

orig_video = cv2.VideoCapture(
    'data/lesson8/meetings.mp4'
)

while True:
    success, img = orig_video.read()

    if not success:
        break

    frame_resize = cv2.resize(img, None, fx=0.2, fy=0.2)

    # при conf 0.2 - 0.25 либо невидит телефон / путает спинку кресла с рюкзаком. Для разных случаев
    model_results = model.predict(frame_resize, device='cpu', conf=0.20, iou=0.5)
    # model_results = model.predict(frame_resize, device='cpu', conf=0.25)

    # Для практики iou=0.2 - 3 человека, так как площадь соприкосновения людей по бокам больше, чем значение iou
    # model_results = model.predict(frame_resize, device='cpu', conf=0.20, iou=0.2)

    frame_result = model_results[0]
    current_frame_plot = frame_result.plot()

    cv2.imshow('img', current_frame_plot)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

orig_video.release()

# =================================================================================================

# Завдання 2
# =================================================================================================
# Відкрийте відео з файлу data\lesson8\meetings.mp4
# Застосуйте детекцію та почніть показувати відео з моменту, коли людей стало 5

while True:
    success, img = orig_video.read()

    if not success:
        break

    frame_resize = cv2.resize(img, None, fx=0.2, fy=0.2)
    model_results = model.predict(frame_resize, device='cpu', conf=0.25, classes=[0])

    frame_result = model_results[0]
    current_frame_plot = frame_result.plot()

    people_count = len(frame_result.boxes.cls)

    if people_count >= 5:
        cv2.imshow('img', current_frame_plot)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

orig_video.release()
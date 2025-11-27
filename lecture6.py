import ultralytics
import cv2

# # import model
# model = ultralytics.YOLO('yolov8s.pt')
# # #
# cap = cv2.VideoCapture(0)
# success, img = cap.read()
# #
# # predict
# results = model.predict(img,
#                             device='cpu',
#                             conf=0.1)
# result = results[0]
#
# # class names by model
# names = result.names
#
# # objects
# print(result.boxes.cls)
#
# # probability
# print(result.boxes.conf)
#
# # graphic plot
# res_img = result.plot()
# cv2.imshow('res1', res_img)
#
# cv2.waitKey(0)
# print(result)


# while True:
#     success, img = cap.read()
#
#     if not success:
#         break
#
#     results = model.predict(img,
#                             device='cpu',
#                             conf=0.1)
#
#     result = results[0]
#
#     res_img = result.plot()
#
#     cv2.imshow('img', res_img)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()

# first object
# box = result.boxes
# print(box)
#
# # coordinates
# xyxy = box.xyxy[0]
# x1, y1, x2, y2 = map(int, xyxy)
# roi = img[y1:y2, x1:x2]
#
# cv2.imshow('object', roi)
# cv2.waitKey(0)

# Завдання 1
# =======================================================================================================
# Отримайте перший кадр з файлу data\lesson8\animals.mp4 та виведіть його на екран.
# Проведіть детекцію об’єктів зо допомогою YOLO та виведіть результати.
# Змініть параметри моделі conf та iou і подивіться як це впливає на результат.
# Отримайте рамки для кожного об’єкта, виріжіть їх та виведіть як окремі зображення

# orig_img = cv2.VideoCapture(
#     'data/lesson8/animals.mp4'
# )
#
# success, img = orig_img.read()
# img_resize = cv2.resize(img, None, fx=0.5, fy=0.5)
#
# cv2.imshow('orig_img', img_resize)
# cv2.waitKey(0)
#
# model = ultralytics.YOLO('yolov8s.pt')
# model_results = model.predict(img, device='cpu', conf=0.25, iou=0.7)
#
# frame_model_result = model_results[0]
# print(frame_model_result)
#
# # objects
# print(frame_model_result.boxes)
#
# for i in range(len(frame_model_result.boxes)):
#     xyxy = frame_model_result.boxes.xyxy[i]
#     x1, y1, x2, y2 = map(int, xyxy)
#     roi = img[y1:y2, x1:x2]
#
#     cv2.imshow(f'img{i}', roi)
#
# cv2.waitKey(0)

# =======================================================================================================

# model = ultralytics.YOLO('yolov8s.pt')
#
# while True:
#     success, img = orig_video.read()
#
#     if not success:
#         break
#
#     img_resize = cv2.resize(img, None, fx=0.5, fy=0.5)
#
#     model_results = model.predict(img_resize , device='cpu', conf=0.25, iou=0.7)
#     frame_model_result = model_results[0]
#
#     res_img = frame_model_result.plot()
#     cv2.imshow('img', res_img)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# orig_video.release()

# Завдання 2
# Напишіть програму по відстеженню об’єкта на відео.
# Відкрийте відео з файлу data\lesson8\animals.mp4 та виведіть на екран результат детекції.
# Попросіть користувача ввести ID об’єкта, який потрібно відслідковувати
# Для всіх наступних кадрів проведіть детекцію, отримайте рамку для об’єкта з потрібним ID та виведіть її на екран.
# Додатково показуйте оригінальне відео. Скористайтесь для роботи model.track()
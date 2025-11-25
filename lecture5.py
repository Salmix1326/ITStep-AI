import cv2


# # open video
# cap = cv2.VideoCapture(
#     0 # file path / 0 -- computer camera
# )
#
# # video data:
# # frame size
# print(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))) # frame width
# print(int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))) # frame height
# # fps
# print(int(cap.get(cv2.CAP_PROP_FPS))) # fps

# save video:
# codec (video type(mp4, avi, xvd))
# fourcc = cv2.VideoWriter_fourcc(*"MP4V")
#
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = int(cap.get(cv2.CAP_PROP_FPS))
#
# writer = cv2.VideoWriter(
#     'result.mp4', # video path
#     fourcc, # codec
#     fps,
#     (width, height)
# )

# write GRAYSCALE video
# writer = cv2.VideoWriter(
#     'result.mp4', # video path
#     fourcc, # codec
#     fps,
#     (width, height)
#     isColor=False # if video-frame is colored
# )

# get next frame
# success, img = cap.read()
# success -- true/false if frame has returned

# video streaming
# while True:
#     success, img = cap.read()
#
#     if not success:
#         break
#
#     # frame rendering
#
#     # video to GRAYSCALE
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     # gauss blur
#     gauss = cv2.GaussianBlur(
#         gray,
#         ksize = (9,9),
#         sigmaX=1
#     )
#
#     # binarization
#     adapt = cv2.adaptiveThreshold(
#         gray,
#         255,
#         cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#         cv2.THRESH_BINARY,
#         11,
#         2
#     )
#
#     cv2.imshow('camera', img)
#     cv2.imshow('adapt', adapt)
#
#     # save frame from video
#     # writer.write(img)
#
#     # wait while press some key for 1 millisecond
#     # cv2.waitKey(1)
#     # if pressed q key -- stop video
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# close program
# cap.release()
# writer.release()


# Завдання 1
# =========================================================================================
# Виведіть відео з файлу data\lesson7\text.mp4 на екран та збережіть в новий файл.
# Змініть розмір зображення.
# Проведіть бінарізацію кадрів та збережіть в новий файл.

# orig_video = cv2.VideoCapture(
#     'data/lesson7/text.mp4'
# )
#
# # save video:
# # codec (video type(mp4, avi, xvd))
# fourcc = cv2.VideoWriter_fourcc(*"MP4V")

# width = int(orig_video.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(orig_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = int(orig_video.get(cv2.CAP_PROP_FPS))

# orig_video.set(cv2.CAP_PROP_FRAME_WIDTH, int(width*0.5))
# orig_video.set(cv2.CAP_PROP_FRAME_HEIGHT, int(height*0.5))

# writer = cv2.VideoWriter(
#     'result_text.mp4',  # video path
#     fourcc,  # codec
#     fps,
#     (width // 2, height // 2),
#     isColor=False
# )
#
# while True:
#     success, img = orig_video.read()
#
#     if not success:
#         break
#
#     # frame rendering
#     new_frame = cv2.resize(img, None, fx=0.5, fy=0.5)
#     new_frame_gray = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)
#
#     new_frame_blur = cv2.GaussianBlur(new_frame_gray, (3,3), 5)
#
#     new_frame_bilateral_filter = cv2.bilateralFilter(new_frame_gray, 7, 75, 75)
#
#     adapt = cv2.adaptiveThreshold(
#             new_frame_blur,
#             255,
#             cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#             cv2.THRESH_BINARY,
#             11,
#             2
#         )
#
#     adapt_bilat = cv2.adaptiveThreshold(
#         new_frame_bilateral_filter,
#         255,
#         cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#         cv2.THRESH_BINARY,
#         11,
#         3
#     )
#
#     cv2.imshow("adapt_bilat", adapt_bilat)
#
#     # save frame from video
#     writer.write(adapt_bilat)
#
#     # wait while press some key for 1 millisecond
#     # cv2.waitKey(1)
#     # if pressed q key -- stop video
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# orig_video.release()
# writer.release()

# Завдання 2
# =========================================================================================
# Відкрийте відео з файлу data\lesson7shapes.mp4.
# Проведіть виділення країв на кадрах та збережіть в новий файл.

# orig_video = cv2.VideoCapture(
#     'data/lesson7/shapes.mp4'
# )
#
# # save video:
# # codec (video type(mp4, avi, xvd))
# fourcc = cv2.VideoWriter_fourcc(*"MP4V")
#
# width = int(orig_video.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(orig_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = int(orig_video.get(cv2.CAP_PROP_FPS))
#
# writer = cv2.VideoWriter(
#     'result_shape_red.mp4',  # video path
#     fourcc,  # codec
#     fps,
#     (width // 2, height // 2),
#     isColor=False
# )
#
# while True:
#     success, img = orig_video.read()
#
#     if not success:
#         break
#
#     # frame rendering
#     new_frame = cv2.resize(img, None, fx=0.5, fy=0.5)
#     new_frame_hsv = cv2.cvtColor(new_frame, cv2.COLOR_BGR2HSV)
#
#     # 260 - 280 (130 - 140)
#     lower1 = (0, 40, 100)
#     upper1 = (20, 255, 255)
#
#     lower2 = (170, 40, 100)
#     upper2 = (180, 255, 255)
#
#     result_hsv1 = cv2.inRange(new_frame_hsv, lower1, upper1)
#     result_hsv2 = cv2.inRange(new_frame_hsv, lower2, upper2)
#     result_red = cv2.bitwise_or(result_hsv1, result_hsv2)
#
#     # adapt_bilat = cv2.adaptiveThreshold(
#     #     new_frame_hsv,
#     #     255,
#     #     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#     #     cv2.THRESH_BINARY,
#     #     11,
#     #     3
#     # )
#
#     cv2.imshow("new_frame", new_frame)
#     cv2.imshow("result_red", result_red)
#
#     # save frame from video
#     writer.write(result_red)
#
#     # wait while press some key for 1 millisecond
#     # cv2.waitKey(1)
#     # if pressed q key -- stop video
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# orig_video.release()
# writer.release()

# clearing noise with local-avg method
# cv2.fastNlMeansDenoising(#img name, parameterdif, windowfordif, searchforneighbors)

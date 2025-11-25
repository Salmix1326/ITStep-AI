# Модуль 3. Generative AI, LLM
# Тема: Langchain. Частина 3
# Завдання 1
# ===========================================================================================
# Відкрийте відео з файлу data\lesson7\meter.mp4.
# Проведіть бінарізацію кадрів та збережіть в новий файл.
# Можливо очистіть від шуму або наведіть різкість через bilateralFilter
import cv2

orig_video_meter = cv2.VideoCapture(
    'data/lesson7/meter.mp4'
)

# save video:
# codec (video type(mp4, avi, xvd))
fourcc = cv2.VideoWriter_fourcc(*"MP4V")

width = int(orig_video_meter.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(orig_video_meter.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(orig_video_meter.get(cv2.CAP_PROP_FPS))

writer = cv2.VideoWriter(
    'result_meter.mp4',  # video path
    fourcc,  # codec
    fps,
    (width // 2, height // 2),
    isColor=False
)

while True:
    success, img = orig_video_meter.read()

    if not success:
        break

    # frame rendering
    new_frame = cv2.resize(img, None, fx=0.5, fy=0.5)
    new_frame_gray = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)

    # filters
    new_frame_blur = cv2.GaussianBlur(new_frame_gray, (31, 31), 3)
    frame_bilateral_filter = cv2.bilateralFilter(new_frame_gray, 7, 75, 75)

    adapt_gauss_blur = cv2.adaptiveThreshold(
        new_frame_blur,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        2
    )

    adapt_bilat = cv2.adaptiveThreshold(
        frame_bilateral_filter,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        3
    )

    cv2.imshow("new_frame_blur", new_frame_blur)
    cv2.imshow("frame_bilateral_filter", frame_bilateral_filter)
    cv2.imshow("adapt_gauss_blur", adapt_gauss_blur)
    cv2.imshow("adapt_bilat", adapt_bilat)

    # save frame from video
    writer.write(adapt_bilat)

    # wait while press some key for 1 millisecond
    # cv2.waitKey(1)
    # if pressed q key -- stop video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

orig_video_meter.release()
writer.release()
import cv2
import numpy as np

# img = cv2.imread(
#     'data/lesson1/cameraman.png',
#     cv2.IMREAD_GRAYSCALE
# )

# print(img)
# print(type(img))
# print(img.shape)
# print(img.dtype)
#
# new_img = cv2.resize(img, (500, 500))
#
# cv2.imshow(
#     'image',
#     new_img
# )
#
# cv2.waitKey(0)
# print('End')
#
# img = cv2.imread(
#     'data/lesson1/cameraman.png',
#     cv2.IMREAD_GRAYSCALE
# )
#
# img = cv2.resize(img, (500, 500))
#
# new_img = img.astype(np.int16)
# new_img += 80
#
# mask_255 = new_img > 255
# new_img[mask_255] = 255
# mask_0 = new_img < 0
# new_img[mask_0] = 0
#
# new_img = np.clip(new_img, 0, 255)
#
# new_img = new_img.astype(np.uint8)
#
# cv2.imshow('new', new_img)
#
# cv2.waitKey(0)

# Завдання 1
# Відкрийте зображення data/Lenna.png.
# Виведіть на екран розмір зображення, тип даних, максимальну та мінімальну інтенсивність пікселів,
# саме зображення з підписом.

# img = cv2.imread(
#     'data/lesson1/Lenna.png',
#     cv2.IMREAD_GRAYSCALE
# )
#
# new_img = cv2.resize(img, (500, 500))
#
# print(img.shape)
# print(img.dtype)
# print(f"Num min: {np.min(img)}. Num max: {np.max}")
# print(img)
#
# cv2.imshow('new', new_img)
# cv2.waitKey(0)

#==============================================================================================
# Завдання 2
# Відкрийте зображення data/Lenna.png.
# Виведіть на екран такі зображень:
# Верхній лівий кут розміром 100х50
# Центральний квадрат розміром 100х100
# Верхню половину
# Нижню половину
# Ліву половину
# Праву половину

# img = cv2.imread(
#     'data/lesson1/Lenna.png',
#     cv2.IMREAD_GRAYSCALE
# )
#
# new_img = cv2.resize(img, (500, 500))
#
# left_up_segment = new_img[:101, :201]
# center_segment = new_img[200:400, 200:400]
# upper_half = new_img[:250]
# down_half = new_img[250:]
# left_half = new_img[:, :250]
# right_half = new_img[:, 250:]
#
# cv2.imshow("left_up_segment", left_up_segment)
# cv2.imshow("center_segment", center_segment)
# cv2.imshow("upper_half", upper_half)
# cv2.imshow("down_half", down_half)
# cv2.imshow("left_half", left_half)
# cv2.imshow("right_half", right_half)
# cv2.waitKey(0)

#==============================================================================================
# Завдання 3
# Відкрийте зображення data/Lenna.png. Створіть наступні зображення

# img = cv2.imread(
#     'data/lesson1/Lenna.png',
#     cv2.IMREAD_GRAYSCALE
# )
#
# img = cv2.resize(img, (500, 500))
#
# img[:20] = 0
# img[-30:] = 255
# cv2.imshow("upper_black_line", img)
# cv2.imshow("down_white_line", img)
# cv2.waitKey(0)
#=========================
# img[:, :20] = 0
# img[:, 480:] = 0
# cv2.imshow("black_lines_on_sides", img)
# cv2.waitKey(0)
#=========================
# img[:50] = 0
# img[450:] = 0
# img[:, :50] = 0
# img[:, 450:] = 0
# cv2.imshow("black_lines_square", img)
# cv2.waitKey(0)

# ==============================================================================================
# Завдання 4
# Відкрийте зображення data/Lenna.png.
# Створіть маску для пікселів з інтенсивністю більше 128 та виведіть її.
# Також виведіть заперечення цієї маски.
# На оригінальному зображенні, усі пікселі які не відповідають масці замініть на 0 та виведіть результат

img = cv2.imread(
    'data/lesson1/cameraman.png',
    cv2.IMREAD_GRAYSCALE
)

img = cv2.resize(img, (500, 500))
#
# mask_128 = img > 128
#
# print(mask_128)
#
# # img[mask_128] = 0
# # img[~mask_128] = 0
#
cv2.imshow("edit_mask_img", img)
# cv2.waitKey(0)

import utils

@utils.trackbar_decorator(gamma_parameter=(1, 30))
def gamma_correction(image, gamma_parameter):
    gamma_parameter /= 10
    result = 255 * (image/255) ** gamma_parameter
    result = result.astype(np.uint8)

    return result


new_img = gamma_correction(img)

cv2.imshow("edit_img", new_img)
cv2.waitKey(0)



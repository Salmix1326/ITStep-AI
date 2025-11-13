# Курс: AI+Python
# Модуль 12. Структури даних
# Тема: Стеки. Частина 2
#===================================================================================
# Завдання 1
# Відкрийте зображення data/Lenna.png.
# Прочитайте маски data/mask1.png та data/mask2.png.
# Усі пікселі які не відповідають маскам замінити на 0, перед застосуванням змініть тип даних у масці на bool
import cv2
import numpy as np


img = cv2.imread(
    "data/lesson1/Lenna.png",
    cv2.IMREAD_GRAYSCALE
)

mask1 = cv2.imread(
    "data/lesson1/mask1.png",
    cv2.IMREAD_GRAYSCALE
)

mask2 = cv2.imread(
    "data/lesson1/mask2.png",
    cv2.IMREAD_GRAYSCALE
)

# Об’єднайте дві маски в одну, скористайтесь cv2.bitwise_or() та виведіть результат
union_masks = cv2.bitwise_or(mask1, mask2)
cv2.imshow("masks", union_masks)

# mask1
mask1 = mask1.astype(bool)
segment1 = np.zeros_like(img)
segment1[mask1] = img[mask1]

# mask2
mask2 = mask2.astype(bool)
segment2 = np.zeros_like(img)
segment2[mask2] = img[mask2]

# mask1 і mask2
union_masks = union_masks.astype(bool)
segment3 = np.zeros_like(img)
segment3[union_masks] = img[union_masks]

cv2.imshow("segment1", segment1)
cv2.imshow("segment2", segment2)
cv2.imshow("segment3", segment3)
cv2.waitKey(0)

#===================================================================================
# Завдання 2
# Виведіть зображення. Підберіть самостійно межі

img = cv2.imread(
    "data/lesson1/baboo.jpg",
    cv2.IMREAD_GRAYSCALE
)

img[:10] = 255
img[-210:] = 255
img[:, :60] = 255
img[:, -60:] = 255

cv2.imshow("res", img)
cv2.waitKey(0)
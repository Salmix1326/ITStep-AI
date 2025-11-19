import cv2


# img = cv2.imread('data/lesson2/lego.jpg', cv2.IMREAD_COLOR)
#
# # red_part = img[:, :, 2]
# # green_part = img[:, :, 1]
# # blue_part = img[:, :, 0]
#
# # only red color
# # img[:, :, 1] = 0 # green - 0
# # img[:, :, 0] = 0 # blue - 0
#
# # img - bgr
# cv2.imshow('bgr', img)
#
# # hsv
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# print(hsv.shape)
# print(hsv.dtype)
#
# mask_blue = cv2.inRange(hsv,
#                         (100, 200, 140),
#                         (130, 255, 255)
# )
#
# cv2.imshow('mask_blue', mask_blue)
# cv2.waitKey(0)


# Модуль 12. Аналіз даних
# Тема: Стеки. Частина 2
# ===================================================================================
# Завдання 1
# Відкрийте зображення data/lesson2/marbles.png.
# Використайте кольорову сегментацію для отримання масок до кульок:
# синього кольору
# зеленого і червоного
# чорного
# білого
# усіх кульок

# marbles_all_orig = cv2.imread('data/lesson2/marbles.png', cv2.IMREAD_COLOR)
# cv2.imshow('original', marbles_all_orig)
#
# marbles_hsv = cv2.cvtColor(marbles_all_orig, cv2.COLOR_BGR2HSV)
#
# blue_mask = cv2.inRange(marbles_hsv, (90, 220, 10), (125, 255, 255))
# green_mask = cv2.inRange(marbles_hsv, (50, 170, 10), (70, 255, 255))
#
# red_mask1 = cv2.inRange(marbles_hsv, (0, 200, 30), (5, 255, 255))
# red_mask2 = cv2.inRange(marbles_hsv, (175, 220, 10), (180, 255, 255))
# red_mask = cv2.bitwise_or(red_mask1, red_mask2)
#
# red_green_mask = cv2.bitwise_or(red_mask, green_mask)
#
# grey_marbles = cv2.cvtColor(marbles_all_orig, cv2.COLOR_BGR2GRAY)
#
# black_mask = cv2.inRange(grey_marbles, 0, 20)
# white_mask = cv2.inRange(grey_marbles, 230, 255)
#
# blue_mask = blue_mask.astype(bool)
# marbles_all_orig[blue_mask] = 255
#
# cv2.imshow('white-blue', marbles_all_orig)
# cv2.waitKey(0)

# Завдання 2
# =======================================================================================================
# Відкрийте зображення data/lesson2/cell.png.
# Покращте зображення за допомогою вирівнювання гістограми.
# Оскільки зображення кольорове, вам доведеться зробити наступні кроки:
# перевести зображення в LAB
# розбити зображення на канали l, a та b
# вирівняти гістограму для l
# зібрати канали назад в зображення
# перевести результат назад в BGR
# Порівняйте результати для 2 алгоритмів.

cell_img = cv2.imread('data/lesson2/cell.png', cv2.IMREAD_COLOR)
cv2.imshow('cell_orig', cell_img)

cell_img_lab = cv2.cvtColor(cell_img, cv2.COLOR_BGR2LAB)

l =  cell_img_lab[:, :, 0]
a =  cell_img_lab[:, :, 1]
b =  cell_img_lab[:, :, 2]

new_l = cv2.equalizeHist(l)

cell_img_lab[:, :, 0] = new_l
cell_img_lab = cv2.cvtColor(cell_img_lab, cv2.COLOR_LAB2BGR)

cv2.imshow('cell-lab', cell_img_lab)
cv2.waitKey(0)
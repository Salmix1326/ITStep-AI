# Завдання 1
# Відкрийте зображення data\lesson2\darken.png.
# Проведіть з ним наступні операції, переведіть його в HSV формат та обробіть канал Value наступними способами:
import cv2
import numpy as np


orig_img = cv2.imread('data/lesson2/darken.png', cv2.IMREAD_COLOR)

# застосуйте вирівнювання гістограм
hsv_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2HSV)

h =  hsv_img[:, :, 0]
s =  hsv_img[:, :, 1]
v =  hsv_img[:, :, 2]

new_v = cv2.equalizeHist(v)
hsv_img[:, :, 2] = new_v

hsv_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)



# збільшіть значення десь на 20-50%, оскільки тут результат буде типу float32 та явно вийде за межі [0-255]
hsv_img_coef = cv2.cvtColor(orig_img, cv2.COLOR_BGR2HSV)
hsv_img_coef[:, :, 2] = hsv_img_coef[:, :, 2].astype(np.float32)

new_v_coef = 0.5
hsv_img_coef[:, :, 2] = hsv_img_coef[:, :, 2] * new_v_coef

# застосуйте np.clip(value, 0, 255) та value.astype(np.uint8)
hsv_img_coef[:, :, 2] = np.clip(hsv_img_coef[:, :, 2], 0, 255)
hsv_img_coef[:, :, 2] = hsv_img_coef[:, :, 2].astype(np.uint8)

# Виведіть результати обох обробок на екран
hsv_img_coef = cv2.cvtColor(hsv_img_coef, cv2.COLOR_HSV2BGR)
cv2.imshow('hsv_coef', hsv_img_coef)
cv2.imshow('hsv_equalizeHist', hsv_img)
cv2.waitKey(0)
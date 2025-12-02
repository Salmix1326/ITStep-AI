# Модуль 2. Комп’ютерний зір
# Тема: opencv. Частина 2
# Завдання 1
# ==============================================================================================
# Відкрийте зображення data/lesson_seg/tumor1.jpg
# Проведіть сегментацію зображення використовуючи модель data/lesson_seg/brain-tumor-seg.jpg
# Визначте площу пухлини в пікселях.
# Визначте площу в см квадратних (1 піксель – 0,0025)
# В залежності від площі присвойте пухлині певний тип
# <10 – small
# 10-25 – middle
# >25 – large
# Покажіть пухлину – за допомогою маски усі лишні пікселі зробіть 0, а як назву зображення використайте її тип
import numpy as np
import ultralytics
import cv2


model = ultralytics.YOLO('data/lesson_seg/brain-tumor-seg.pt')
orig_img = cv2.imread('data/lesson_seg/tumor1.jpg')

# результаты модели
model_results = model.predict(orig_img)
orig_model_result = model_results[0]
orig_model_result_plot = orig_model_result.plot()

# работа с маской
orig_model_result_mask = orig_model_result.masks.data[0]
orig_model_result_mask = orig_model_result_mask.numpy()

# площадь
orig_model_result_mask_area_px = orig_model_result_mask.sum()
orig_model_result_mask_area_sm = orig_model_result_mask_area_px * 0.0025
print(orig_model_result_mask_area_sm)

if orig_model_result_mask_area_sm < 10:
    tumor_type = "small tumor"

elif 25 >= orig_model_result_mask_area_sm >= 10:
    tumor_type = "middle tumor"

else:
    tumor_type = "large tumor"

# подготовка маски для отображения части фото
orig_model_result_mask = orig_model_result_mask.astype(np.uint8)
orig_model_result_mask *= 255
orig_model_result_mask = orig_model_result_mask.astype(bool)

orig_img[~orig_model_result_mask] = 0

# отображение
cv2.imshow(f'{tumor_type}', orig_img)
cv2.waitKey(0)
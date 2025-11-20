# Модуль 12. Аналіз даних
# Тема: Стеки. Частина 2
# ========================================================================================
# Завдання 1
# Відкрийте зображення data/lesson3/notes.png.
# Проведіть наступні дії:
# проведіть бінарізацію(звичайну та адаптивну)
# застосуйте розмиття(гаусове) візьміть ядра 3, 5, 11 та sigmaX 0, 2, 10
# повторіть бінарізацію, але перед тим застосуйте bilateral filter
import cv2
#
# img = cv2.imread('data/lesson3/notes.png', cv2.IMREAD_GRAYSCALE)
#
# threshold = 100
#
# res = img.copy()
# mask = res > threshold
# res[mask] = 255
# res[~mask] = 0
#
# res1 = cv2.adaptiveThreshold(img,
#                              255,
#                              cv2.ADAPTIVE_THRESH_MEAN_C,
#                              cv2.THRESH_BINARY,
#                              11,
#                              2)
#
# res3 = cv2.adaptiveThreshold(img,
#                              255,
#                              cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                              cv2.THRESH_BINARY,
#                              11,
#                              2)
#
# res2 = cv2.GaussianBlur(
#     img,
#     (3,3),
#     2
# )
#
# bilateral = cv2.bilateralFilter(img,
#                                 d=5,
#                                 sigmaColor=75,
#                                 sigmaSpace=75,
#                                 )
#
# cv2.imshow('bilateral', bilateral)
#
# cv2.imshow('original', img)
# cv2.imshow('bin', res)
# cv2.imshow('gauss', res1)
# cv2.waitKey(0)


# Завдання 2
# Відкрийте зображення data/lesson3/sudoku.jpg.
# Проведіть для нього бінарізацію, а саме
# CLAHE
# гаусове розмиття
# адаптивна бінарізація
# NLMean
# Самостійно підберіть параметри, збережіть результат.
# Порівняйте результати для гаусової та середньої адаптивної бінарізації

# img = cv2.imread('data/lesson3/sudoku.jpg', cv2.IMREAD_GRAYSCALE)
#
# res = cv2.GaussianBlur(
#     img,
#     (5,5),
#     4
# )
#
# res1 = cv2.adaptiveThreshold(img,
#                              255,
#                              cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                              cv2.THRESH_BINARY,
#                              11,
#                              2)
#
# res2 = cv2.adaptiveThreshold(img,
#                              255,
#                              cv2.ADAPTIVE_THRESH_MEAN_C,
#                              cv2.THRESH_BINARY,
#                              11,
#                              2)
#
# bilateral = cv2.bilateralFilter(img,
#                                 d=3,
#                                 sigmaColor=75,
#                                 sigmaSpace=75,
#                                 )
#
# res3 = cv2.adaptiveThreshold(bilateral,
#                              255,
#                              cv2.ADAPTIVE_THRESH_MEAN_C,
#                              cv2.THRESH_BINARY,
#                              9,
#                              2)
#
# cv2.imshow('bilateral', bilateral)
# cv2.imshow('bilateral_bin', res3)
# cv2.imshow('original', img)
# cv2.imshow('GAUSS', res)
# cv2.imshow('adaptiveThresholdGAUSSIAN', res1)
# cv2.imshow('adaptiveThresholdMEAN', res2)
# cv2.waitKey(0)


# Завдання 3
# Використовуючи utils.trackbar_decorator Побудуйте class
# ThresholdingParameterSelector для підбору параметрів для
# адаптивної бінарізації.
# Методи:
# o run(img, **kwargs) – головний метод який
# запускає застосовує усі перетворення до
# зображення і повертає маску.
# Решту парметрів підберіть самостійно
# Можливі методи:
# o _apply_blur(img, ksize, sigmaX)
# o _apply_bilateral(img, d, sigmaS, sigmaC)
# o _apply_threshold(img, ksize, C)
# o _apply_denoising(img, h, search_size, tamplate_size)
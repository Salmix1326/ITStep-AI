# Завдання 1
# ============================================================================================
# Відкрийте зображення data/lesson3/sonet.png.
import cv2

img = cv2.imread('data/lesson3/sonet.png', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('data/lesson3/sonet_noised.png', cv2.IMREAD_GRAYSCALE)

# Проведіть бінарізацію.
orig_img_values = img.copy()

threshold = 110
mask = orig_img_values > threshold
orig_img_values[mask] = 255
orig_img_values[~mask] = 0

# розмиття або наведення різкості -- очищеня шумів

# # гаусове розмиття
gauss_blur_img_orig = cv2.GaussianBlur(
    img,
    (3, 3),   # розмір ядра
    1.5       # чим більше тим більше розмиття
)

# # двосторонній фільтр
bilateral_img_orig = cv2.bilateralFilter(
    img,
    d=5,  # розмір ядра
    sigmaColor=65,   # наскільки зберігати різкість кольору
    sigmaSpace=65,   # те ж саме що й в GaussianBlur
)

# адаптивна бінарізація
adapt_bin_orig_gauss = cv2.adaptiveThreshold(img,
                                   255,
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY,
                                   5,
                                   3
                                   )

adapt_bin_gauss_with_gauss_blur = cv2.adaptiveThreshold(gauss_blur_img_orig,
                                   255,
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY,
                                   3,
                                   0.5
                                   )

adapt_bin_gauss_with_bilateralFilter = cv2.adaptiveThreshold(bilateral_img_orig,
                                   255,
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY,
                                   7,
                                   0.6
                                   )

adapt_bin_orig_mean = cv2.adaptiveThreshold(img,
                                   255,
                                   cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY,
                                   7,
                                   2
                                   )

cv2.imshow('orig', img)

cv2.imshow('gauss_blur_img_orig', gauss_blur_img_orig)
cv2.imshow('bilateral_img_orig', bilateral_img_orig)

cv2.imshow('default_bin_orig', orig_img_values)
cv2.imshow('adapt_bin_orig_gauss', adapt_bin_orig_gauss)
cv2.imshow('adapt_bin_orig_mean', adapt_bin_orig_mean)

cv2.imshow('adapt_bin_gauss_with_gauss_blur', adapt_bin_gauss_with_gauss_blur)
cv2.imshow('adapt_bin_gauss_with_bilateralFilter', adapt_bin_gauss_with_bilateralFilter)
cv2.waitKey(0)
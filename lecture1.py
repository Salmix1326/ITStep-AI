import time
import numpy as np

# array = np.array([1, 2, 3, 4, 5])
#
# print(array)
# print(array.shape)
# print(array.dtype)
#
# array = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])

# print(array)
# print(array.shape)
# print(array.dtype)
#
# N = 10_000_000
# nums_list = list(range(N))
# nums_array = np.array(range(N))
#
# start = time.time()
# res = sum(nums_list)
# end = time.time()
#
# start1 = time.time()
# res1 = sum(nums_list)
# end1 = time.time()

# Модуль 2. Комп’ютерний зір
# Тема: Масиви. Частина 1
#=============================================================================================
# Завдання 1
# Створіть масив з числами від 1 до 10. Виведіть його, його розмір, тип даних.
# Змініть розмір масиву на (5, 2). Знову виведіть масив, розмір та тип даних

# array = np.array(range(1, 11))
# print(array)
# print(array.shape)
# print(array.dtype)
# new_array = array.reshape(5, 2)
# print(new_array)

#=============================================================================================
# Завдання 2
# Створіть масив:
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# Використовуючи індекси виведіть:
# ● число 7
# ● другий рядок
# ● останній стовпчик
# ● праву половину
# ● жовту область
# ● замініть жовту область на -1
# ● зробіть перший стовпчик таким самим як і другий

# array = np.arange(1, 13)
# array.reshape(3, 4)
#
# print(array[1, 2])
# print(array[1])
# print(array[-1])
# res = array[:, 2:]
# print(res)
# print(array[1:, 1:3])
# array[1:, 1:3] = 0
# print(array)
# array[:, 0] = array[:, 1]
# print(array)

#=============================================================================================
# Завдання 3
# У масиві з попереднього завдання створіть маску для чисел які більші за 6. З її допомогою:
# ● виведіть кількість чисел більших за 6
# ● виведіть самі числа
# ● до кожного числа яке відповідає масці додайте 10
# ● кожне число що не відповідає масці помножте на -1
# ● замініть ці числа які відповідають масці на відповідні
# їм з масиву
# 1 0 1 0
# 0 1 0 1
# 1 0 1 0

# mask = array > 6
# print(mask)
# print(np.sum(mask))
# print(array[mask])
#
# array[mask] += 10
# print(array[mask])
#
# array[~mask] *= -1
#
# array = np.zeros(12)
# array[::2] = 1
# res = array.reshape(3,4)
# print(res)


# Завдання 4
# Створіть масив
# -10 24 35
# 250 -6 7
# 12 180 11
# -2 -45 -26
# Усі числа менші за 0 замініть на 0.
# Усі числа більші за 100 замініть на 100


# Завдання 5
# Створіть масив та виведіть його тип даних
# 100 120 200 250 10
# Додайте до кожного числа 50 та виведіть результат.
# Створіть такий самий масив але з типом uint8
# Знову додайте 50 та виведіть результат
# Зробіть так щоб обчислення працювали правильно, якщо
# число виходить більшим за 255 то зробіть його 255

# nums = np.array([100, 120, 200, 250, 10])
# nums += 50
# print(nums)
#
# nums = np.array([100, 120, 200, 250, 10], dtype=np.uint8)
# nums += 50
# print(nums)
#
# new_nums = nums.astype(np.uint64)
# new_nums += 50
# print(new_nums)
#
# mask = new_nums > 255
#
# new_nums[mask] = 255
#
#
# new_nums = new_nums.astype(np.uint8)
# print(new_nums)


# Завдання 6
# Створіть масив типу uint8
# 10 4 25 40 200
# |Помножте всі значення на 2. Результат має бути типу
# uint8 а всі значення в діапазоні 0-255
# Помножте всі значення на 1.5. Результат має бути типу
# uint8 а всі значення в діапазоні 0-255

nums = np.array([10, 4, 25, 40, 200], dtype=np.uint8)
new_nums = nums.astype(np.uint64)
print(nums)
new_nums *= 2
print(new_nums)
# mask = new_nums > 255
# new_nums[mask] = 255
# print(new_nums)
# nums = new_nums.astype(np.uint8)
# print(nums)
#
# nums = np.array([10, 4, 25, 40, 200], dtype=np.uint8)
# new_nums = nums.astype(np.float32)
# print(nums)
# new_nums *= 1.5
# print(new_nums)
# mask = new_nums > 255
# new_nums[mask] = 255
# print(new_nums)
# nums = new_nums.astype(np.uint8)
# print(nums)
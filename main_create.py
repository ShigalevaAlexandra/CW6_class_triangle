import sys
sys.path.append("/path/to/classes")

from classes.class_TriangleChecker import TriangleChecker

# Функция обработки строки
def is_number(str):
    try:
        float(str)
        return float(str)
    except ValueError:
        return str

print("Введите длины сторон треугольника:\n")
size_mas = 3
user_enter_mas = [input() for sides in range(size_mas)]

for sides in range(size_mas):
    user_enter_mas[sides] = is_number(user_enter_mas[sides])

first_length, second_length, third_length = (
    user_enter_mas[0], user_enter_mas[1], user_enter_mas[2])

new_triangle = TriangleChecker([first_length, second_length, third_length])
print("\n", new_triangle.is_triangle())


#coding: utf-8
if area_circle > area_square:
        return "Площадь круга больше площади квадрата."
    elif area_square > area_circle:
        return "Площадь квадрата больше площади круга."
    else:
        return "Площади круга и квадрата равны."
radius = float(input("Введите радиус круга: "))
side = float(input("Введите сторону квадрата: "))

result = compare_areas(radius, side)
print(result)
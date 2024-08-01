# import random
#
# def genNumbers(numbers: int, chars: int):
#     random_number = []
#     letters = ['a', 'b', 'e', 'k', 'm', 'h',
#                'o', 'p', 'c', 't', 'y', 'x']
#     for i in range(numbers):
#         nn = random.randint(0,9)
#         random_number.append(nn)
#
#     for j in range(chars):
#         cc = random.choice(letters)
#         random_number.append(cc.upper())
#
#     print(*random_number, sep='')
#
# genNumbers(4, 3)

# def hex2int(input_numbers: int):
#     result = int(input_numbers.lower(), 16)
#     return result
#
# def int2hex(input_numbers: str):
#     result = hex(input_numbers)[2:]
#     return result
#
#
#
# print(hex2int('deadb'))
# print(int2hex(123))


# class MyCar:
#     Name_Class = 'Машина моей мечты'
#
#     def __init__ (self, car_brand, speed_car, color_car, price_car, height_car, width_car):
#         self.car_brand = car_brand
#         self.speed_car = speed_car
#         self.color_car = color_car
#         self.price_car = price_car
#         self.height_car = height_car
#         self.width_car = width_car
#
#     def drive(self):
#         speed_drive = 100
#         print(f"Еду со скоростью {speed_drive} км в час.")
#
#     def accelerate (self):
#         speed_accelerate = 50
#         print(f"Разгоняюсь со скоростью {speed_accelerate} метров в секунду.")
#
#     def braking(self):
#         speed_braking = 75
#         print(f"Торможу со скоростью {speed_braking} метров в секунду.")
#
# def main():
#     my_favorite_car = MyCar('Mercedes-Benz SLS AMG', 400, 'Зеленый', 17_000_000,
#                             1400, 2565.8)
#     print(f"Наименование класса: {my_favorite_car.Name_Class}\n")
#     print("Характеристики машины: ")
#     print(f"Марка авто -> {my_favorite_car.car_brand}")
#     print(f"Скорость авто, {my_favorite_car.speed_car} км в час.")
#     print(f"Цвет авто, {my_favorite_car.color_car}")
#     print(f"Цена авто, {my_favorite_car.price_car} рублей.")
#     print(f"Высота авто, {my_favorite_car.height_car} мм.")
#     print(f"Ширина авто, {my_favorite_car.width_car} мм")
#
#
# if __name__ == "__main__":
#     main()
#
#
#
# old_my_car = MyCar('BMW x7', 350, 'Синий', 12_000_000,
#                             2000, 2865.4)
#
# print(f"Наименование класса: {old_my_car.Name_Class}\n")
# print("Характеристики машины: ")
# print(f"Марка авто -> {old_my_car.car_brand}")
# print(f"Скорость авто, {old_my_car.speed_car} км в час.")
# print(f"Цвет авто, {old_my_car.color_car}")
# print(f"Цена авто, {old_my_car.price_car} рублей.")
# print(f"Высота авто, {old_my_car.height_car} мм.")
# print(f"Ширина авто, {old_my_car.width_car} мм")

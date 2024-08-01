# small_bottle = int(input("Введите количество МАЛЕНЬКИХ бутылок: "))
# big_bottle = int(input("Введите количество БОЛЬШИХ бутылок: "))
#
# less_liter_price = 0.1
# more_liter_price = 0.25
#
# total_small_price = small_bottle * less_liter_price
# total_big_price = big_bottle * more_liter_price
# total_price = total_small_price + total_big_price
#
# f_money = "${:.2f}".format(total_price)
# print("Итоговая сумма: ", f_money)


# num = int(input("Введите число: "))
#
# total = num * (num + 1) / 2
# print(int(total))

# import math
# s = int(input("Введите длину стороны: "))
# n = int(input("Введите количетво сторон: "))
#
# total = (n * s**2)/(4 * math.tan(math.pi/n))
# print(total)

sec = int(input("Введите количекство секунд: "))

in_minute = 60
in_hour = 60 * 60
in_day = 60 * 60 * 24

out_day = sec // in_day
out_hour = (sec - (in_day * out_day)) // in_hour
out_minute = (sec - (in_day * out_day) - (in_hour * out_hour)) // in_minute
out_sec = (sec - (in_day * out_day) - (in_hour * out_hour) - (in_minute * out_minute))

print(f'{out_day} {out_hour}:{out_minute}:{out_sec}')



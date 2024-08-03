import random

class Neuron:
    def __init__ (self, w):
        self.w = w

    def onestep(self, x): # Функция активации
        if x >= 0:
            return 1
        else:
            return 0

    def у(self, x):
        s = 0
        for i in range(random_len):
            s += Xi[i] * Wi[i]
        return s

# Задаем случайную длину списка для создания вектора
random_len = random.randint(1, 10)

# Задаем порог срабатывания
bias = 10

# Задаем входной вектор
Xi = [random.randint(0, 1) for i in range(random_len)]

# Задаем вектор весов
Wi = [random.randint(0, 10) for i in range(random_len)]
n = Neuron(Wi)
S = n.у(Xi) - bias

# Вывводим результат
print('Результат работы сумматора :: S =', S)
print('Результат работы функции активации :: Y =', n.onestep(S))
if n.onestep(S):
  print("Идем на работу")
else:
  print("Сидим дома")
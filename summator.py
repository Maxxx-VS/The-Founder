import numpy as np


class Neuron:
    def __init__ (self, w):
        self.w = w

    def onestep(self, x): # Функция активации
        if x >= 0:
            return 1
        else:
            return 0

    def у(self, x) :
        s = np.dot(self.w, x) # Суммируем входы и добавляем смещение b
        return s


bias = 5 # порог срабатывания
# Задаем входной вектор
Xi = np.array([1, 0, 0, 1])

# Задаем вектор весов
Wi = np.array([5, 4, 1, 1])
n = Neuron(Wi)
S = n.у(Xi) - bias
print('S =', S)
print('Y =', n.onestep(S))
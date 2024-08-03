import numpy as np

class Neuron:
    def __init__ (self, w):
        self.w = w

    def у(self, x) :
        s = np.dot(self.w, x)
        return s

# Задаем входной вектор
Xi = np.array([1, 0, 0, 1])

# Задаем вектор весов
Wi = np.array([5, 4, 1, 1])
n = Neuron(Wi)
print('S = ', n.у(Xi))
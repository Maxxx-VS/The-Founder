import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)

def sigmoid(alpha):
    return 1 / ( 1 + np.exp(-alpha * x) )

dpi = 80
fig, ax = plt.subplots(dpi = dpi, figsize=(512 / dpi, 384 / dpi))
ax.set_title("Сигмоида с параметром a", fontsize=16)
ax.set_xlabel("S", fontsize=14)
ax.set_ylabel("Y", fontsize=14)

plt.plot(x, sigmoid(0.5), 'r-')
plt.plot(x, sigmoid(1.0), 'g-')
plt.plot(x, sigmoid(2.0), 'b-')

plt.legend(['a = 0.5', 'a = 1.0', 'a = 2.0'], loc = 'upper left')
plt.show()
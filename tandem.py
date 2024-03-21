import numpy as np
import matplotlib.pyplot as plt
import math

E0 = 1
lambda0 = 1.31
left = -400 * lambda0  # левая граница графика
right = 400 * lambda0  # правая граница графика
step_lambda = 1e-3  # шаг по длине волны
step = 1e-3  # шаг по ∆l
delta_lambda = 20e-3
delta_l2 = 200 * lambda0  # фиксированно
range_lambda = np.arange(lambda0 - 5 * delta_lambda, lambda0 + 5 * delta_lambda, step_lambda)  # диапазон волн
delta_l1 = np.arange(left, right + step, step)
k = (2 * math.pi) / range_lambda
print("Диапазон λ:", range_lambda)
I = 0
for i in range(len(range_lambda)):
    E = (E0 ** 2) * (math.exp(-(((range_lambda[i] - lambda0) ** 2) / (2 * ((2 * delta_lambda) ** 2))))) #распределение Гаусса
    I += E * (4 * (np.cos(k[i] * delta_l1) + np.cos(k[i] * delta_l2)) + 2 * (np.cos(
        k[i] * (delta_l1 + delta_l2)) + np.cos(k[i] * (delta_l1 - delta_l2))))
print("Интенсивность:", I)
plt.plot(delta_l1, I)
plt.show()

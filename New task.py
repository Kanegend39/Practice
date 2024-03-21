import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.signal import hilbert

E0 = 1
lambda0 = 1.31
left = 185 * lambda0  # левая граница графика
right = 215 * lambda0  # правая граница графика
step_lambda = 1e-3  # шаг по длине волны
step = 1e-3  # шаг по ∆l
delta_lambda = 20e-3
delta_l2 = 200 * lambda0  # фиксированно
range_lambda = np.arange(lambda0 - 5 * delta_lambda, lambda0 + 5 * delta_lambda, step_lambda)  # диапазон волн
delta_l1 = np.arange(left, right + step, step)
k = (2 * math.pi) / range_lambda
print("Диапазон λ:", range_lambda)
I = 0
I_new = 0
for i in range(len(range_lambda)):
    E = (E0 ** 2) * (math.exp(-(((range_lambda[i] - lambda0) ** 2) / (2 * ((2 * delta_lambda) ** 2))))) #распределение Гаусса
    I += E * (4 * (np.cos(k[i] * delta_l1) + np.cos(k[i] * delta_l2)) + 2 * (np.cos(
        k[i] * (delta_l1 + delta_l2)) + np.cos(k[i] * (delta_l1 - delta_l2))))
I_new = np.abs(hilbert(I)) #преобразование Гильберта
print("Интенсивность:", I)
print("Интенсивность после преобразования Гильберта:", I_new)
plt.plot(delta_l1, I)
plt.plot(delta_l1, I_new)
a = np.sqrt(I ** 2 + I_new ** 2) #амплитуда
print(a)
comp = np.arctan2(I_new, I)
print("ωt + φ:", comp)
approximated_line = np.polyfit(delta_l1, comp, 1)
print("k и b прямой:", approximated_line)
plt.plot(delta_l1, delta_l1 * approximated_line[0] + approximated_line[1])
plt.plot(delta_l1, comp)
plt.plot(delta_l1, comp - (delta_l1 * approximated_line[0] + approximated_line[1]))
plt.show()


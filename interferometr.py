import numpy as np
import matplotlib.pyplot as plt
import math


def interferometr(E0, lambda0, left, right, step_lambda, step, delta_lambda):
    range_lambda = np.arange(lambda0 - 5 * delta_lambda, lambda0 + 5 * delta_lambda, step_lambda)  # диапазон волн
    delta_l = np.arange(left, right + step, step)
    print(delta_l)
    k = (2 * math.pi) / range_lambda
    print("Диапазон λ:", range_lambda)
    I = 0
    for i in range(len(range_lambda)):
        E = (E0 ** 2) * (
            math.exp(-(((range_lambda[i] - lambda0) ** 2) / (2 * ((2 * delta_lambda) ** 2)))))  # распределение Гаусса
        I += 2 * E * (np.cos(2 * k[i] * delta_l))
    print("Интенсивность:", I)
    #plt.plot(delta_l, I)
    #plt.show()
    return delta_l, I

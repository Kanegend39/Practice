import numpy as np
import matplotlib.pyplot as plt
import math


def tandem(E0, lambda0, left, right, step_lambda, step, delta_lambda, delta_l2):
    range_lambda = np.arange(lambda0 - 5 * delta_lambda, lambda0 + 5 * delta_lambda, step_lambda)  # диапазон волн
    delta_l1 = np.arange(left, right + step, step)
    k = (2 * math.pi) / range_lambda
    print("Диапазон λ:", range_lambda)
    I = 0
    for i in range(len(range_lambda)):
        E = (E0 ** 2) * (
            math.exp(-(((range_lambda[i] - lambda0) ** 2) / (2 * ((2 * delta_lambda) ** 2)))))  # распределение Гаусса
        I += E * (4 * (np.cos(k[i] * delta_l1) + np.cos(k[i] * delta_l2)) + 2 * (np.cos(
            k[i] * (delta_l1 + delta_l2)) + np.cos(k[i] * (delta_l1 - delta_l2))))
    print("Интенсивность:", I)
    # plt.plot(delta_l1, I)
    # plt.show()
    return delta_l1, I
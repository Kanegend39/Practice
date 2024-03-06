import numpy as np
import matplotlib.pyplot as plt
import math

E0 = 1
lambda0 = 1.31
left = -400 * lambda0
right = 400 * lambda0
step_lambda = 1 * (10 ** (-3))
step = 0.001
delta_lambda = 20 * (10 ** (-3))
lambda_ = np.arange(lambda0 - delta_lambda, lambda0 + delta_lambda + step_lambda, step_lambda)
delta_l = np.arange(left, right + step, step)
k = (2 * math.pi) / lambda_
print("Диапазон λ:", lambda_)
I1 = 0
E = 0
for i in range(len(lambda_)):
    E = (E0 ** 2) * (math.e ** (-(((lambda_[i] - lambda0) ** 2) / (2 * (delta_lambda ** 2)))))
    I1 += 2 * E * (np.cos(2 * k[i] * delta_l))
print("Интенсивность:", I1)
plt.plot(delta_l, I1)
plt.show()

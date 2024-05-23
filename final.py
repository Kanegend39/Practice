import A_f
import reading_excel
import matplotlib.pyplot as plt
import math
import numpy as np

amplitude = A_f.grafik_a_delta_phi()[1]
print()
print(list(amplitude))
lambda_0 = 1.55 * 1e3
phi = np.arange(1, 51, 1.)
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'white', 'grey', 'pink', 'brown', 'orange']
for i in range(5):
    for j in range(10):
        phi[(i % 5) * 10 + j] = 2 * amplitude[i + j * 5]
calibration = [682.738, 320.328, 140.917, 182.131, 373.196, 25.533, 39.138, 21.322, 23.171, 12.662]
a_s = np.arange(1, 51, 1.)
for i in range(50):
    if i < 10:
        a_s[i] = calibration[i % 10]
    elif i < 20:
        a_s[i] = 2 * calibration[i % 10]
    elif i < 30:
        a_s[i] = 3 * calibration[i % 10]
    elif i < 40:
        a_s[i] = 4 * calibration[i % 10]
    elif i < 50:
        a_s[i] = 5 * calibration[i % 10]
delta_d = (phi * lambda_0) / (2 * math.pi)
betta = delta_d / a_s
betta_sr = sum(betta) / len(betta)
print('βср. =', betta_sr)
summar = 0
for i in range(50):
    summar += (betta[i] - betta_sr) ** 2
sigma = math.sqrt(summar / 49)
print('σ =', sigma)
for i in range(1, 11):
    f = np.polyfit(a_s[i - 1::10], delta_d[i - 1::10], 1)
    plt.plot(a_s[i - 1::10], f[0] * a_s[i - 1::10] + f[1], color=colors[i - 1], label=f'{i} кГц')
    plt.plot(a_s[i - 1::10], delta_d[i - 1::10], 'o', color=colors[i - 1])
    print(f'{i} кГц b =', f[1], 'k =', f[0])
plt.xlabel('As [нм]')
plt.ylabel('delta_d [нм]')
plt.legend(labelcolor='white')
plt.grid(color='cyan', linewidth=0.5)
plt.grid(True)
plt.show()

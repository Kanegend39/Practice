import numpy as np
import reading_excel
from scipy.signal import hilbert
import matplotlib.pyplot as plt
import math


def grafik_a_delta_phi():
    f = np.arange(1, 11, 1)
    amplitude = []
    for i in range(1, 51):
        a = reading_excel.read(f'{i}.xlsx')
        new_delta_phi = a[6]
        if max(new_delta_phi) < min(new_delta_phi):
            amplitude.append(min(new_delta_phi))
        else:
            amplitude.append(max(new_delta_phi))
    return f, amplitude

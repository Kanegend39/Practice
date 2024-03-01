import sys
import numpy as np
import matplotlib.pyplot as plt
import math
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_window.ui', self)
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        E0 = float(self.lineEdit_1.text())
        wavelength = float(self.lineEdit_2.text())
        left = float(self.lineEdit_3.text())
        right = float(self.lineEdit_4.text())
        step = float(self.lineEdit_5.text())
        rg = float(self.lineEdit_6.text())
        dim = 10 ** (-6)
        self.grafik(E0, wavelength, left, right, step, dim, int(rg))

    def grafik(self, E0, wavelength, left, right, step, dim, rg):
        delta_l = np.arange(left * wavelength, (right + step) * wavelength, step)
        wavelength *= 10 ** (-6)
        print(delta_l)
        I = 0
        for i in range(-rg, rg + 1):
            E = (E0 ** 2) * (math.e ** (-(((i * (10 ** (-9))) ** 2)/(2 * (1 * 10 ** (-18))))))
            I += E * (np.cos(((4 * math.pi) / (wavelength + (i * (10 ** (-9)))) * (delta_l * dim))))
        print(I)
        plt.plot(delta_l * dim, 2 * I)
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
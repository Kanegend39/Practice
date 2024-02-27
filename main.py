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
        mass = [self.radioButton_1.isChecked(), self.radioButton_2.isChecked(), self.radioButton_3.isChecked(),
                self.radioButton_4.isChecked()]
        match mass:
            case list() if mass[0]:
                dim = 1
            case list() if mass[1]:
                dim = 10 ** (-3)
            case list() if mass[2]:
                dim = 10 ** (-6)
            case list() if mass[3]:
                dim = 10 ** (-9)
        E0 = float(self.lineEdit_1.text())
        wavelength = float(self.lineEdit_2.text()) * (10 ** -6)
        left = float(self.lineEdit_3.text())
        right = float(self.lineEdit_4.text())
        step = float(self.lineEdit_5.text())
        self.grafik(E0, wavelength, left, right, step, dim)

    def grafik(self, E0, wavelength, left, right, step, dim):
        delta_l = np.arange(left, right, step)
        plt.plot(delta_l * dim, 2 * (E0 ** 2) * np.cos(((4 * math.pi) / wavelength) * (delta_l * dim)))
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())

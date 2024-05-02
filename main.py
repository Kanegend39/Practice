# by Kanegend39
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMainWindow
from PyQt6 import uic
import sys
import numpy as np
import pandas as pd
import matplotlib

import A_V

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import os

# .py files #
import interferometr
import tandem
import New_task
import reading_excel
import A_V
import A_f


# FUNCTION FOR EXCEPTION HANDLEMENT #
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


# I had some problems with exporting to .exe. This condition helped me. #
# If we access a non-existent object, then we change the directory #
# sys._MEIPASS is a temporary folder for PyInstaller #
if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)


# CLASS FOR THE REALIZATION GRAPHS. CANVAS FOR MATPLOTLIB. #
class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=10, height=8, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(1, 1, 1)
        self.axes.set_facecolor('black')
        self.axes.grid(color='cyan', linewidth=0.5)
        self.axes.grid(True)
        super(MplCanvas, self).__init__(fig)


class MplCanvas_3D(FigureCanvas):
    def __init__(self, parent=None, width=10, height=8, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(1, 1, 1, projection='3d')
        self.axes.set_facecolor('white')
        self.axes.grid(color='cyan', linewidth=0.5)
        self.axes.grid(True)
        super(MplCanvas_3D, self).__init__(fig)

# MAIN WINDOW #
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = uic.loadUi('main.ui', self)
        self.show()
        self.pushButton_1.clicked.connect(self.click_1)
        self.pushButton_2.clicked.connect(self.click_2)
        self.pushButton_3.clicked.connect(self.click_3)

    def click_1(self):
        self.layout.hide()
        self.test = Test()

    def click_2(self):
        self.layout.hide()
        self.test = Theory()

    def click_3(self):
        self.layout.hide()
        self.test = Results()


class Results(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = uic.loadUi('results.ui', self)
        self.canvas1 = MplCanvas(self, width=10, height=8, dpi=100)
        self.canvas2 = MplCanvas(self, width=10, height=8, dpi=100)
        self.canvas3 = MplCanvas_3D(self, width=10, height=8, dpi=100)
        self.toolbar1 = NavigationToolbar(self.canvas1, self)
        self.toolbar2 = NavigationToolbar(self.canvas2, self)
        self.toolbar3 = NavigationToolbar(self.canvas3, self)
        self.form1.addWidget(self.toolbar1)
        self.form2.addWidget(self.canvas1)
        self.form3.addWidget(self.toolbar2)
        self.form4.addWidget(self.canvas2)
        self.form5.addWidget(self.toolbar3)
        self.form6.addWidget(self.canvas3)
        self.pushButton.clicked.connect(self.cancel)
        self.grafik1()
        self.grafik2()
        self.grafik3()
        self.show()

    def grafik1(self):
        a = A_V.grafik_a_v()
        approximated_line_1 = np.polyfit(a[0], a[1][:5], 1)
        approximated_line_2 = np.polyfit(a[0], a[1][5:10], 1)
        approximated_line_3 = np.polyfit(a[0], a[1][10:15], 1)
        approximated_line_4 = np.polyfit(a[0], a[1][15:20], 1)
        approximated_line_5 = np.polyfit(a[0], a[1][20:25], 1)
        approximated_line_6 = np.polyfit(a[0], a[1][25:30], 1)
        approximated_line_7 = np.polyfit(a[0], a[1][30:35], 1)
        approximated_line_8 = np.polyfit(a[0], a[1][35:40], 1)
        approximated_line_9 = np.polyfit(a[0], a[1][40:45], 1)
        approximated_line_10 = np.polyfit(a[0], a[1][45:50], 1)
        self.canvas1.axes.plot(a[0], a[0] * approximated_line_1[0] + approximated_line_1[1], 'violet', label='1 кГц')
        self.canvas1.axes.plot(a[0], a[0] * approximated_line_2[0] + approximated_line_2[1], 'white', label='2 кГц')
        self.canvas1.axes.plot(a[0], a[0] * approximated_line_3[0] + approximated_line_3[1], 'yellow', label='3 кГц')
        self.canvas1.axes.plot(a[0], a[0] * approximated_line_4[0] + approximated_line_4[1], 'silver', label='4 кГц')
        self.canvas1.axes.plot(a[0], a[0] * approximated_line_5[0] + approximated_line_5[1], 'purple', label='5 кГц')
        self.canvas1.axes.plot(a[0], a[0] * approximated_line_6[0] + approximated_line_6[1], 'lime', label='6 кГц')
        self.canvas1.axes.plot(a[0], a[0] * approximated_line_7[0] + approximated_line_7[1], 'coral', label='7 кГц')
        self.canvas1.axes.plot(a[0], a[0] * approximated_line_8[0] + approximated_line_8[1], 'indigo', label='8 кГц')
        self.canvas1.axes.plot(a[0], a[0] * approximated_line_9[0] + approximated_line_9[1], 'crimson', label='9 кГц')
        self.canvas1.axes.plot(a[0], a[0] * approximated_line_10[0] + approximated_line_10[1], 'green', label='10 кГц')
        self.canvas1.axes.legend(labelcolor='white')

    def grafik2(self):
        a = A_f.grafik_a_delta_phi()
        self.canvas2.axes.plot(a[0], a[1][0::5], 'violet', label='1 Вольт')
        self.canvas2.axes.plot(a[0], a[1][1::5], 'white', label='2 Вольта')
        self.canvas2.axes.plot(a[0], a[1][2::5], 'yellow', label='3 Вольта')
        self.canvas2.axes.plot(a[0], a[1][3::5], 'silver', label='4 Вольта')
        self.canvas2.axes.plot(a[0], a[1][4::5], 'purple', label='5 Вольт')
        self.canvas2.axes.legend(labelcolor='white')

    def grafik3(self):
        a1 = A_f.grafik_a_delta_phi()
        a2 = A_V.grafik_a_v()
        self.canvas3.axes.plot(a1[0], a1[1][0::5], a2[0][0], 'violet')
        self.canvas3.axes.plot(a1[0], a1[1][1::5], a2[0][1], 'yellow')
        self.canvas3.axes.plot(a1[0], a1[1][2::5], a2[0][2], 'silver')
        self.canvas3.axes.plot(a1[0], a1[1][3::5], a2[0][3], 'purple')
        self.canvas3.axes.plot(a1[0], a1[1][4::5], a2[0][4], 'crimson')

    def cancel(self):
        self.layout.hide()
        self.test = Main()


# THEORETICAL DATA WIDGET #
class Theory(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = uic.loadUi('theory.ui', self)
        self.canvas = MplCanvas(self, width=10, height=8, dpi=100)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.form_1.addWidget(self.toolbar)
        self.form_2.addWidget(self.canvas)
        self.widget2.hide()
        self.widget3.hide()
        self.comboBox.currentTextChanged.connect(self.change)
        self.show()
        self.pushButton_1.clicked.connect(self.grafik)
        self.pushButton_2.clicked.connect(self.cancel)

    def change(self):
        if self.comboBox.currentText() == 'Tandem':
            self.widget1.hide()
            self.widget3.hide()
            self.widget2.show()
        elif self.comboBox.currentText() == 'Interferometr':
            self.widget2.hide()
            self.widget3.hide()
            self.widget1.show()
        elif self.comboBox.currentText() == 'Phase recovery':
            self.widget2.hide()
            self.widget1.hide()
            self.widget3.show()

    def grafik(self):
        if self.comboBox.currentText() == 'Interferometr':
            a = interferometr.interferometr(self.doubleSpinBox_1.value(), self.doubleSpinBox_2.value(),
                                            self.doubleSpinBox_3.value(), self.doubleSpinBox_4.value(),
                                            self.doubleSpinBox_7.value(), self.doubleSpinBox_5.value(),
                                            self.doubleSpinBox_6.value())
            self.canvas.axes.cla()
            self.canvas.axes.grid(True)
            self.canvas.axes.plot(a[0], a[1], 'blue')
            self.canvas.draw()
            self.toolbar.show()
        elif self.comboBox.currentText() == 'Tandem':
            a = tandem.tandem(self.doubleSpinBox_8.value(), self.doubleSpinBox_9.value(),
                              self.doubleSpinBox_10.value(), self.doubleSpinBox_11.value(),
                              self.doubleSpinBox_14.value(), self.doubleSpinBox_12.value(),
                              self.doubleSpinBox_13.value(), self.doubleSpinBox_15.value())
            self.canvas.axes.cla()
            self.canvas.axes.grid(True)
            self.canvas.axes.plot(a[0], a[1], 'blue')
            self.canvas.draw()
            self.toolbar.show()
        elif self.comboBox.currentText() == 'Phase recovery':
            a = New_task.phase_recovery(self.doubleSpinBox_24.value(), self.doubleSpinBox_25.value(),
                                        self.doubleSpinBox_26.value(), self.doubleSpinBox_27.value(),
                                        self.doubleSpinBox_30.value(), self.doubleSpinBox_28.value(),
                                        self.doubleSpinBox_29.value(), self.doubleSpinBox_31.value(),
                                        self.doubleSpinBox_32.value(), self.doubleSpinBox_33.value())
            self.canvas.axes.cla()
            self.canvas.axes.grid(True)
            self.canvas.axes.plot(a[0], a[1], 'blue')
            self.canvas.axes.plot(a[0], a[2], 'violet')
            self.canvas.axes.plot(a[0], a[3], 'orange')
            self.canvas.draw()
            self.toolbar.show()

    def cancel(self):
        self.layout.hide()
        self.test = Main()


# ERROR HANDLING #
class Error(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = uic.loadUi('FileNotFoundError.ui', self)
        self.button.clicked.connect(self.back)
        self.layout.show()

    def back(self):
        self.layout.hide()


# PRACTICAL DATA WIDGET #
class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = uic.loadUi('test.ui', self)
        self.canvas = MplCanvas(self, width=10, height=8, dpi=100)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.form1.addWidget(self.toolbar)
        self.form.addWidget(self.canvas)

        self.line.setText(excel_file_path[:-5])

        self.button1.clicked.connect(self.loadExcelData)

        self.button2.clicked.connect(self.grafik)

        self.button3.clicked.connect(self.cancel)
        self.show()

    def cancel(self):
        self.layout.hide()
        self.test = Main()

    def loadExcelData(self):
        try:
            excel_file_dir = self.line.text() + '.xlsx'
            df = pd.read_excel(excel_file_dir)
            if df.size == 0:
                return

            df.fillna('', inplace=True)
            self.table.setRowCount(df.shape[0])
            self.table.setColumnCount(df.shape[1])
            self.table.setHorizontalHeaderLabels(df.columns)

            for row in df.iterrows():
                values = row[1]
                for col_index, value in enumerate(values):
                    if isinstance(value, (float, int)) and col_index % 2 != 1:
                        value = '{0:0.0f}'.format(value)
                    tableItem = QTableWidgetItem(str(value))
                    self.table.setItem(row[0], col_index, tableItem)
        except FileNotFoundError:
            self.test = Error()

    def grafik(self):
        try:
            a = reading_excel.read(self.line.text() + '.xlsx')
            self.canvas.axes.cla()  # Clear the canvas.
            if self.checkBox1.isChecked():
                self.canvas.axes.plot(a[0], a[1], 'white')
            if self.checkBox2.isChecked():
                self.canvas.axes.plot(a[0], a[2], 'red')
            if self.checkBox3.isChecked():
                self.canvas.axes.plot(a[0], a[3], 'green')
            if self.checkBox4.isChecked():
                self.canvas.axes.plot(a[0], a[4], 'blue')
            if self.checkBox5.isChecked():
                self.canvas.axes.plot(a[7], a[5], 'violet')
            if self.checkBox6.isChecked():
                self.canvas.axes.plot(a[7][20:-20], a[6][20:-20], 'yellow')
            self.canvas.axes.grid(True)
            self.canvas.draw()
            self.toolbar.show()
        except FileNotFoundError:
            self.test = Error()


if __name__ == '__main__':
    excel_file_path = '1.xlsx'
    app = QApplication(sys.argv)
    test = Main()
    sys.excepthook = except_hook
    sys.exit(app.exec())

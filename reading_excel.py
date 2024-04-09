import openpyxl
import numpy as np
import matplotlib.pyplot as plt

path = "signals.xlsx"
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active
m_row = sheet_obj.max_row
x = np.arange(0, m_row - 1, 1)
grafik_1 = np.arange(0, m_row - 1, 1).astype("float")
grafik_2 = np.arange(0, m_row - 1, 1).astype("float")
grafik_3 = np.arange(0, m_row - 1, 1).astype("float")
grafik_4 = np.arange(0, m_row - 1, 1).astype("float")
print(x)
print(m_row)
for i in range(2, m_row + 1):
    obj_1 = sheet_obj.cell(row=i, column=2)
    grafik_1[i - 2] = obj_1.value
    obj_2 = sheet_obj.cell(row=i, column=4)
    grafik_2[i - 2] = obj_2.value
    obj_3 = sheet_obj.cell(row=i, column=6)
    grafik_3[i - 2] = obj_3.value
    obj_4 = sheet_obj.cell(row=i, column=8)
    grafik_4[i - 2] = obj_4.value
print(grafik_1)
print(grafik_2)
print(grafik_3)
print(grafik_4)
plt.rcParams.update({
    'axes.facecolor': 'black'
})
plt.plot(x, grafik_1, color='white')
plt.plot(x, grafik_2, color='red')
plt.plot(x, grafik_3, color='green')
plt.plot(x, grafik_4, color='blue')
plt.show()
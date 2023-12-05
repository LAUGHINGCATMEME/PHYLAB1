import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

a = np.loadtxt(r"C:\Users\Lenovo\Desktop\Physics Lab 1\PH1123 2023\04. Youngs Moduls\data")  # Path of data here
weight = []
loading = []
unloading = []
for i in a:
    weight.append(i[0])
    loading.append(i[1])
    unloading.append(i[2])

weight = np.array(weight) * 10 ** -3
loading = np.array(loading)
unloading = np.array(unloading)
loading = np.abs(loading - np.max(loading)) * 10 ** -5
unloading = np.abs(unloading - np.max(unloading)) * 10 ** -5


def mxc(x, m, c):
    return m * x + c


param_fit, param_cov = curve_fit(mxc, weight, (loading + unloading)/2)
fitm, fitc = param_fit
errm, errc = np.sqrt(np.diag(param_cov))
plt.plot(weight, mxc(weight, fitm, fitc), label='Best Fit', color='black')
plt.plot(weight, loading, marker='o', linestyle='', color="green", label='loding')
plt.plot(weight, unloading, marker='o', linestyle='', color="red", label='unloading')
plt.xlabel('Weight Added (Kg)')
plt.ylabel('Deflection (m)')
plt.legend()
plt.show()

print(f"Slope is {fitm} +- {errm}    {errm/fitm*100:.2f}%")

length = np.mean(np.array([30])) * 10 ** -2
width = np.mean(np.array([5.58, 5.60, 5.61, 5.62, 5.58, 5.57]) + 0.13 ) * 10 ** -3  # MILLI METERSSSSSSSSSSSSSSSSSSSSSSSSSSS and least count
breath = np.mean(np.array([5])) * 10 ** -2
g = 9.78378
youngs_moduls = g*length**3/(4*fitm*breath*width**3)*10**-9

print(f"Youngs Moduls: {youngs_moduls:.2f} * 10^9 +- {youngs_moduls*math.sqrt((np.std(width)/np.mean(width))**2 + (errm/fitm)**2) + 0.01}")

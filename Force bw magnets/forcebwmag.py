import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Data Gathering
data_array = np.loadtxt(r"C:\Users\Lenovo\Desktop\Force bw magnets\forcebwmag_data.txt")
mass = []
scale = []

for i in data_array:
    mass.append(i[0])
    scale.append(np.mean(i[1:]))


# Data Analysis
zm_vals = list(np.array(scale) - 10 + 0.64 + 0.3)  # Subtractin the Length and adding Diameter
f_vals = list(np.array(mass) + 3)  # Adding plate mass
x_axis = list(np.log10(np.array(zm_vals)))  # SI distance
g = 9.8
y_axis = list(np.log10(np.array(f_vals)))  # SI Force


# Curve Fitting

# Curve fitting
def f_x(x, a, b):
    return a*x + b


param_fit, param_cov = curve_fit(f_x, x_axis, y_axis)
param_error = np.sqrt(np.diag(param_cov))

fitm, fitc = param_fit
errm, errc = param_error


# Result
print(f"m = {fitm} +- {errm} {errm*100/fitm:.2f}%\nc = {fitc} +- {errc:.7} {abs(errc*100/fitc):.2f}%")
bh = 4
plt.plot(np.linspace(0, bh), f_x(np.array(np.linspace(0, bh)), fitm, fitc), color="red")
plt.ylim(0, 3)
plt.xlim(0.000, 1)

plt.plot(x_axis, f_x(np.array(x_axis), fitm, fitc), color="red")
plt.errorbar(x_axis, y_axis, marker='o', linestyle='')
plt.ylabel('log(weight of mass added[g])')
plt.xlabel('log(distance between magnets[cm])')
plt.show()






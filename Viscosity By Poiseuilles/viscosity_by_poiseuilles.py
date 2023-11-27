import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import math

# Inputting Data
r = 0.311 * 10**-3 / 2  # meters
r_err = 0.0005 * 10**-3 / 2
length = 2.54 * 10 ** -2  # meters
length_err = 0.005 * 10 ** -2
rho = 1000  # Kg/m^3
rho_err = 1
g = 9.8  # m/sec^2
g_err = 0.01
v = 0.005  # L
v_err = 0

X_h_array = np.tile(np.array([(58.6+51.9)/2, (51.9+44.9)/2, (44.9+38.6)/2]), 3) * 10 ** -2
Y_tinverse_array = np.array([97.24, 111.74, 131.14, 98.00, 112.66, 131.13, 97.6, 112.07, 131.34]) ** -1


# Curve fitting
def f_x(x, a, b):
    return a*x + b


param_fit, param_cov = curve_fit(f_x, X_h_array, Y_tinverse_array)
param_error = np.sqrt(np.diag(param_cov))

fitm, fitc = param_fit
errm, errc = param_error


# Result
print(f"m = {fitm} +- {errm} {errm*100/fitm:.2f}%\nc = {fitc} +- {errc:.7} {abs(errc*100/fitc):.2f}%")
bh = 0.69
#plt.plot(np.linspace(0, bh), f_x(np.array(np.linspace(0, bh)), fitm, fitc), color="red")
#plt.ylim(0, 0.01)
#plt.xlim(0.000, 0.6)

plt.plot(X_h_array, f_x(np.array(X_h_array), fitm, fitc), color="red")
plt.errorbar(X_h_array, Y_tinverse_array, marker='o', linestyle='')
plt.ylabel('1/t (sec$^{-1}$)')
plt.xlabel('h (m)')
#plt.show()

eta = math.pi*rho*g*r**4/(8*length*v*0.018432797624933675)
print(f"""{length_err*100/length}
{r_err*100/r}
{g_err*100/g}
{v_err*100/v}
{rho_err*100/rho}""")

m = 4.4202744569647956e-05/0.018432797624933675

eta_err = eta * math.sqrt((length_err/length)**2 + (4*r_err/r)**2 + (g_err/g)**2 + (v_err/v)**2 + (rho_err/rho)**2 + m**2)
print(eta_err)



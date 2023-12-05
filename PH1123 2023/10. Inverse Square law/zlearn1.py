import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.optimize import curve_fit


def fx(x, c):
    return c/(x-dist)**2


def mxc(x, m, con):
    return m*x + con


def loop(func, dis, vol, fit_c, n):
    global unsex
    global dist
    if n == 0:
        global_fit_c.append(fit_c)
        return
    n -= 1
    cov = (0.25 + abs(unsex * (2 * fit_c / (dis - dist) ** 3)) ** 2) ** 0.5
    param_fit, param_cov = curve_fit(func, dis, vol, sigma=cov)
    fit_c = param_fit[0]
    loop(func, dis, vol, fit_c, n)


def PLOT(Distancee, Voltagee):
    global dist
    distance_1 = Distancee
    voltage_1 = Voltagee
    loop(fx, distance_1, voltage_1, fit_c=5000, n=40)
    fit_c = global_fit_c[-1]
    cov = (0.25 + abs(unsex * (fit_c / (distance_1 - dist) ** 3)) ** 2) ** 0.5

    # Normal Scale
    plt.plot(np.linspace(0.1, 111, 1000), fx(np.array(np.linspace(0.1, 111, 1000)), c=fit_c), color="red",
             label="Best fit")
    plt.errorbar(distance_1, voltage_1, marker='o', linestyle='', color="red", yerr=cov, fmt='none',
                 ecolor='black', capsize=math.pi, label="Uncertainty")
    plt.plot(distance_1, voltage_1, marker='o', linestyle='', color="black", label="Data Points")
    plt.xlim(0)
    plt.ylim(0, 669)
    plt.xlabel("Distance from source (cm)")
    plt.ylabel("Voltage measured (mV)")
    plt.title("Distance vs Voltage")
    plt.legend()
    plt.show()



global_fit_c = []


d1 = np.array([30, 20, 15, 13, 12, 11, 10.5, 10, 9.5])[4:]
d2 = np.array([9.5, 10, 10.5, 11, 11.5, 12, 13, 15, 20, 25, 30, 40, 50])[:-6]
d3 = np.array([20, 15, 13, 12, 11, 10.5, 10, 9.5])
d4 = np.array([15, 13, 11, 10.5, 10, 9.5, 9.3])

v1 = np.array([3, 6, 16, 28, 41, 64, 83, 113, 146])[4:]
v2 = np.array([489, 403, 309, 234, 186, 150, 107, 61, 23, 12, 8, 5, 3])[:-6]
v3 = np.array([2, 12, 31, 56, 110, 155, 211, 265])
v4 = np.array([3, 8, 28, 39, 53, 66, 72])

DISTANCES = np.array([d1, d2, d3, d4])
VOLTAGE = np.array([v1, v2, v3, v4])

unsex = 0.2
dist = np.mean([6.720807459868055, 6.853248615598878])


for afsd, d in enumerate(DISTANCES):
    PLOT(d, VOLTAGE[afsd])

    distance = d-dist
    voltage = np.log(VOLTAGE[afsd])
    param_fit, param_cov = curve_fit(mxc, distance, voltage)
    fit_m, fit_c = param_fit

    print(fit_m**-1)
    plt.plot(distance, mxc(distance, m=fit_m, con=fit_c), color="red",
             label="Best fit")
    plt.plot(distance, voltage, marker='o', linestyle='', color="black", label="Data Points")
    plt.errorbar(distance, voltage, marker='o', linestyle='', color="red", yerr=[np.array(), np.array()], fmt='none',
                 ecolor='black', capsize=math.pi, label="Uncertainty")
    plt.xlabel("Distance from source (cm)")
    plt.ylabel("Log(Voltage) (mV)")
    plt.title(f"Distance vs Log(Voltage) for E{afsd+1}")
    plt.legend()
    plt.show()



import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def fx(x, dist, c):
    return c/(x-1.5)**2


def mxc(x, m, c):
    return -2*x + c










# Data Inputs
"""
distance_1 = 100-np.arange(0, 86, 5)[:8]
voltage_1 = np.array([73, 81, 90, 102, 116, 132, 152, 177, 211, 260, 324, 394, 469, 501, 534, 566, 603, 662])[:8]"""
voltage_1 = np.array([3, 6, 16, 28, 41, 64, 83, 113, 146])[2:]
distance_1 = np.array([30, 20, 15, 13, 12, 11, 10.5, 10, 9.5])[2:]

cov = np.full((1, 7), 0.5)[0]


param_fit, param_cov = curve_fit(mxc, np.log(voltage_1), distance_1, sigma=cov)
fit_m, fit_c = param_fit



plt.plot(np.log(voltage_1), distance_1, marker='o', linestyle='', color="black", label="Data Points")
plt.plot(np.log(voltage_1), mxc(np.log(voltage_1), m=fit_m, c=fit_c), color="red", label="Theoritical Curve")
plt.errorbar(np.log(voltage_1), distance_1, marker='o', linestyle='', color="red", yerr=0.5, fmt='none', ecolor='black',
             capsize=5, label="Uncertainty")
#plt.xlim(0)
#plt.ylim(0, 669)
print(1/fit_m)
plt.ylabel("Distance from source (cm)")
plt.xlabel("Log(Voltage measured (mV))")
plt.title("Log(Voltage) vs Distance")
plt.legend()
plt.show()

exit()














voltage_1_uperr = voltage_1 + 0.5
voltage_1_downerr = voltage_1 - 0.5
cov = (np.log(voltage_1_uperr) - np.log(voltage_1_downerr)) / 2

param_fit, param_cov = curve_fit(mxc, distance_1, np.log(voltage_1), sigma=cov)
fit_m, fit_c = param_fit



plt.plot(distance_1, np.log(voltage_1), marker='o', linestyle='', color="black", label="Data Points")
plt.plot(distance_1, mxc(distance_1, m=fit_m, c=fit_c), color="red", label="Best fit")
plt.errorbar(distance_1, np.log(voltage_1), marker='o', linestyle='', color="red", yerr=cov, xerr=0.2, fmt='none', ecolor='black',
             capsize=0, label="Uncertainty")
#plt.xlim(0)
#plt.ylim(0, 669)
print(1/fit_m)
plt.xlabel("Distance from source (cm)")
plt.ylabel("Log(Voltage measured (mV))")
plt.title("Distance vs Log(Voltage)")
plt.legend()
plt.show()


















exit()


DISTANCES = np.array([distance_1])
VOLTAGE = np.array([voltage_1])

for EXP_no, distance in enumerate(DISTANCES):
    voltage = VOLTAGE[EXP_no][:12]
    distance = distance[:12]

    param_fit, param_cov = curve_fit(fx, distance, voltage)
    param_error = np.sqrt(np.diag(param_cov))
    dist, c = param_fit
    d = param_error[0]

    plt.plot(distance_1[12:], voltage_1[12:], marker='v', linestyle='', color="green", label="Excluded Data Points")
    plt.plot(distance, voltage, marker='o', linestyle='', color="red", label="Data Points")
    plt.plot(np.linspace(0.1, 111, 1000), fx(np.array(np.linspace(0.1, 111, 1000)), dist=dist, c=c), color="red", label="Best Fit Curve")
    plt.errorbar(distance_1[12:], voltage_1[12:], yerr=0.5, xerr=0.5, fmt='none', ecolor='black')
    plt.errorbar(distance, voltage, yerr=0.5, xerr=0.5, fmt='none', ecolor='black')
    plt.xlim(0, 111)
    plt.ylim(0, 800)
    plt.xlabel("Distance from source (cm)")
    plt.ylabel("Voltage measured (mV)")
    #print(f"μ = {fitm1} +- {errm1}    {errm1*100/fitm1:.2f}%")


print(dist, c)
plt.legend()
#plt.show()


def fx(x, dist, c):
    return c/(x-0.01*dist)**2


distance_1 = 100-np.array([85.0, 82.5, 80, 77.5, 75, 70, 60, 45, 25, 0])
voltage_1 = np.array([377, 244, 155, 113, 90, 62, 36, 17, 9, 4])
voltage_1_uncertanity = np.linspace(0.5, 0.5, 10)
DISTANCES = np.array([distance_1])
VOLTAGE = np.array([voltage_1])
UNCERTANITY = np.array([voltage_1_uncertanity])

for EXP_no, distance in enumerate(DISTANCES):
    voltage = VOLTAGE[EXP_no]
    distance = distance
    uncertanity = UNCERTANITY[EXP_no]

    param_fit, param_cov = curve_fit(fx, distance, voltage, sigma=uncertanity)
    param_error = np.sqrt(np.diag(param_cov))
    dist, c = param_fit
    dist_err, c_err = param_error

    plt.plot(distance_1, voltage_1, marker='o', linestyle='', color="green", label="Data Points")
    plt.errorbar(distance, voltage, marker='o', linestyle='', color="red", yerr=0.5, xerr=0.5, fmt='none', ecolor='black')
    plt.plot(np.linspace(0.1, 111, 1000), fx(np.array(np.linspace(0.1, 111, 1000)), dist=dist, c=c), color="red", label="Best fit")
    plt.xlim(0, 111)
    plt.ylim(0, 400 )
    plt.xlabel("Distance from source (cm)")
    plt.ylabel("Voltage measured (mV)")
    #print(f"μ = {fitm1} +- {errm1}    {errm1*100/fitm1:.2f}%")

plt.title("Distance vs Voltage")
plt.legend()
plt.show()
print(dist, c)


















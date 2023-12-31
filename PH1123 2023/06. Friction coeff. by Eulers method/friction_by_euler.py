import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import math


plate = 20
turn0_T1 = np.array([2, 5, 10, 20]) + plate
turn0_T2 = np.array([31, 34.5, 52, 67]) + plate
turn1_T1 = turn0_T1.copy()
turn1_T2 = np.array([125, 130, 167, 176]) + plate
turn2_T1 = turn0_T1.copy()
turn2_T2 = np.array([260, 308, 350, 445]) + plate


def f_x_1(x, mu):
    return x*math.exp(mu*math.pi)


def f_x_3(x, mu):
    return x*math.exp(mu*3*math.pi)


def f_x_5(x, mu):
    return x*math.exp(mu*5*math.pi)


# Curve fits
param_fit, param_cov = curve_fit(f_x_1, turn0_T1, turn0_T2)
param_error = np.sqrt(np.diag(param_cov))
fitm1 = param_fit[0]
errm1 = param_error[0]
plt.plot(turn0_T1, turn0_T2, marker='o', linestyle='', color="red")
plt.plot(np.linspace(0, np.max(turn0_T1), 100), f_x_1(np.linspace(0, np.max(turn0_T1), 100), fitm1), color="red")
print(f"μ = {fitm1} +- {errm1}    {errm1*100/fitm1:.2f}%")

param_fit, param_cov = curve_fit(f_x_3, turn1_T1, turn1_T2)
param_error = np.sqrt(np.diag(param_cov))
fitm2 = param_fit[0]
errm2 = param_error[0]
plt.plot(turn1_T1, turn1_T2, marker='o', linestyle='', color="green")
plt.plot(np.linspace(0, np.max(turn1_T1), 100), f_x_3(np.linspace(0, np.max(turn1_T1), 100), fitm2), color="green")
print(f"μ = {fitm2} +- {errm2}    {errm2*100/fitm2:.2f}%")

param_fit, param_cov = curve_fit(f_x_5, turn2_T1, turn2_T2)
param_error = np.sqrt(np.diag(param_cov))
fitm3 = param_fit[0]
errm3 = param_error[0]
plt.plot(turn2_T1, turn2_T2, marker='o', linestyle='', color="blue")
plt.plot(np.linspace(0, np.max(turn2_T1), 100), f_x_5(np.linspace(0, np.max(turn2_T1), 100), fitm3), color="blue")
print(f"μ = {fitm3} +- {errm3}    {errm3*100/fitm3:.2f}%")


# Output graph
plt.xlim(0)
plt.xlabel('T1/g (gm)')
plt.ylabel('T2/g (gm)')
plt.show()

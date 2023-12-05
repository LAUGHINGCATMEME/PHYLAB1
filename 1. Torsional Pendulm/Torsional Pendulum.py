import numpy as np
import matplotlib.pyplot as plt

#######################3 INPUTS #####################3
# Of Setup
diameter_of_wire = np.array([])
L = np.array([84, 84.1, 84.1])
# Of Motor
rod_length = 1  # mm
rod_thickness = 1  # mm
rod_diameter = 1  # mm
wheel_outer_diameter = 1  # mm
wheel_thickness = 1  # mm


D = [[21.5, 21.5, 21.5, 21.5, 21.5], [35.5, 35.5, 35.5, 35.5, 35.5], [31, 31, 31]]
D_err = [np.std(j) for j in D]
D = np.array([np.mean(j) for j in D])
time_taken = [[3.9/10, 3.93/10, 3.93/10, 4.4/11, 4.43/10], [4.6/10, 4.55/10, 4.6/10, 4.25/9, 4.16/9], [5.68/13, 5.69/13, 5.66/13]]
time_taken_err = [np.std(j) for j in time_taken]
time_taken = np.array([np.mean(j) for j in time_taken])

x_axis = 1/D + 1/(np.mean(L) - D)
y_axis = 1/time_taken**2
plt.errorbar(x_axis, y_axis, label='error', color='black', marker='o', linestyle='', yerr=time_taken**2*time_taken_err)
plt.plot(x_axis, y_axis, label='Data Points', color='red', marker='o', linestyle='')
plt.legend()
plt.xlabel('1/D + 1/(L-D)')
plt.ylabel('1/T^2')
plt.show()









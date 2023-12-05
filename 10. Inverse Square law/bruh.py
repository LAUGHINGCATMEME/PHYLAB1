from scipy.odr import RealData, Model, ODR
import numpy as np
import matplotlib.pyplot as plt

# Create a RealData object
d0 = 100 - np.arange(0, 60, 5)
d1 = np.array([30, 20, 15, 13, 12, 11, 10.5, 10, 9.5])
d2 = np.array([9.5, 10, 10.5, 11, 11.5, 12, 13, 15, 20, 25, 30, 40, 50])
d3 = np.array([20, 15, 13, 12, 11, 10.5, 10, 9.5])
d4 = np.array([15, 13, 11, 10.5, 10, 9.5, 9.3])

v0 = np.array([73, 81, 90, 102, 116, 132, 152, 177, 211, 260, 324, 394])
v1 = np.array([3, 6, 16, 28, 41, 64, 83, 113, 146])
v2 = np.array([489, 403, 309, 234, 186, 150, 107, 61, 23, 12, 8, 5, 3])
v3 = np.array([2, 12, 31, 56, 110, 155, 211, 265])
v4 = np.array([3, 8, 28, 39, 53, 66, 72])


DISTANCES = np.array([d0, d1, d2, d3, d4])
VOLTAGE = np.array([v0, v1, v2, v3, v4])

n = 0
distance = DISTANCES[n]
voltage = VOLTAGE[n]


def inverse_square(params, x):
    c, d = params
    return c / (x - d)**2


x_var = distance
y_var = voltage
x_err = np.full(int(distance.shape[0]), 0.5)
y_err = np.full(int(distance.shape[0]), 0.5)

data = RealData(x_var, y_var, sx=x_err, sy=y_err)

# Create a Model object
quad_model = Model(inverse_square)

# Set up ODR with the model and data
odr_instance = ODR(data, quad_model, beta0=[600000, 6])  # Corrected the number of initial guesses

# Run the regression
out = odr_instance.run()

# Print the results
print("Optimized Parameters:", out.beta)
print("Parameter Errors:", out.sd_beta)

# Plot the data and the fitted curve
x_fit = np.linspace(min(x_var), max(x_var), 1000)
y_fit = inverse_square(out.beta, x_fit)

plt.plot(x_fit, y_fit, label='Theoretical Fit')

plt.errorbar(x_var, y_var, marker='o', linestyle='', xerr=0.5, yerr=0.5, color="black", ecolor='black', capsize=1, label="Data Points")
plt.xlabel('Distance')
plt.ylabel('Voltage')
plt.legend()
plt.show()


# Extract the distance and voltage data for the selected dataset
distance = DISTANCES[n] - out.beta[1]
voltage = VOLTAGE[n]


# Define the linear model function
def mxc(params, x):
    m, c, b = params
    return -m * x + c


# Set up ODR with the model and data
odr_instance = ODR(RealData(np.log(distance), np.log(voltage), sx=0.5/distance, sy=0.5/voltage), Model(mxc), beta0=[-1, 1, 1])  # Adjusted sx for log distance

# Run the regression
out = odr_instance.run()
print("Optimized Parameters:", out.beta)
print("Parameter Errors:", out.sd_beta)

# Plot the data and the fitted curve on the log-log scale
np.log(distance+0.5)-np.log(distance)

plt.errorbar(np.log(distance), np.log(voltage), marker='o', linestyle='', xerr=[-np.log(distance-0.5)+np.log(distance), np.log(distance+0.5)-np.log(distance)], yerr=[-np.log(voltage-0.5)+np.log(voltage), np.log(voltage+0.5)-np.log(voltage)], color="black", ecolor='black', capsize=1, label="Data Points")
x_fit = np.linspace(min(np.log(distance)), max(np.log(distance)), 1000)
y_fit = mxc(out.beta, x_fit)
plt.plot(x_fit, y_fit, label='Linear Fit')
plt.xlabel('Log(Distance)')
plt.ylabel('Log(Voltage)')
plt.legend()
plt.show()

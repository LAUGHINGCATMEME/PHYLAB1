import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Read data from the text file
filename = 'data.txt'
data = np.genfromtxt(filename)

# Extract columns
time = data[:, 0]
amplitude = data[:, 1]


# Define the function to fit
def func(x, A, alpha, omega, phi, c):
    return A * np.exp(alpha * x) * np.sin(omega * x + phi) + c


# Initial guess for the parameters
initial_guess = [1.0, -0.1, 1.0, 0.0, 0.0]
print(len(time))
# Fit the data using curve_fit
params, covariance = curve_fit(func, time, amplitude, p0=initial_guess)

# Extract the fitted parameters
A_fit, alpha_fit, omega_fit, phi_fit, c_fit = params

# Generate the fitted curve
amplitude_fit = func(time, A_fit, alpha_fit, omega_fit, phi_fit, c_fit)

# Plot the original data and the fitted curve
plt.plot(time, amplitude, label='Data points', marker='o', linestyle='')
plt.plot(time, amplitude_fit, label='Fitted Curve')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Data Plot with Curve Fit')
plt.legend()
plt.show()

# Display the fitted parameters
"""print("Fitted Parameters:")
print(f"A: {A_fit}")
print(f"Alpha: {alpha_fit}")
print(f"Omega: {omega_fit}")
print(f"Phi: {phi_fit}")
print(f"C: {c_fit}")"""

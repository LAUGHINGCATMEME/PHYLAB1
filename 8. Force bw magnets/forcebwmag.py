import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.odr import RealData, Model, ODR

# Data Gathering
data_array = np.loadtxt(r"forcebwmag_data.txt")
mass = []
scale = []

for i in data_array:
    mass.append(i[0])
    scale.append(np.mean(i[1:]))


# Data Analysis
zm_vals = np.array(scale) - 10 + 0.64 + 0.3  # Subtractin the Length and adding Diameter
f_vals = np.array(mass) + 3  # Adding plate mass



def inverse_square_square(params, x):
    c, d = params
    return c / (x - d)**4


x_var = np.array(zm_vals)
y_var = np.array(f_vals)
x_err = np.full(int(zm_vals.shape[0]), 0.05)
y_err = np.full(int(f_vals.shape[0]), 1)

data = RealData(x_var, y_var, sx=x_err, sy=y_err)

# Create a Model object
quad_model = Model(inverse_square_square)

# Set up ODR with the model and data
odr_instance = ODR(data, quad_model, beta0=[5000, -0.1])  # Corrected the number of initial guesses

# Run the regression
out = odr_instance.run()

# Print the results
print("Optimized Parameters:", out.beta)
print("Parameter Errors:", out.sd_beta)

# Plot the data and the fitted curve
x_fit = np.linspace(min(x_var), max(x_var), 1000)
y_fit = inverse_square_square(out.beta, x_fit)

plt.plot(x_fit, y_fit, label='Theoretical Fit')

plt.errorbar(x_var, y_var, marker='o', linestyle='', xerr=0.05, yerr=1, color="black", ecolor='black', capsize=1, label="Data Points")
plt.xlabel('Distance (cm)')
plt.ylabel('Weight Added (g)')
plt.legend()
plt.show()


# Extract the distance and voltage data for the selected dataset

# Define the linear model function
def mxc(params, x):
    m, c, b = params
    return -4 * np.log(np.exp(x) + b) + c


# Set up ODR with the model and data
odr_instance = ODR(RealData(np.log(x_var), np.log(y_var), sx=0.05/x_var, sy=1/y_var), Model(mxc), beta0=[-1, 1, -1])  # Adjusted sx for log distance

# Run the regression
out = odr_instance.run()
print("Optimized Parameters:", out.beta)
print("Parameter Errors:", out.sd_beta)

# Plot the data and the fitted curve on the log-log scale
np.log(y_var+1)-np.log(y_var)

plt.errorbar(np.log(x_var), np.log(y_var), marker='o', linestyle='', xerr=[-np.log(x_var-0.05)+np.log(x_var), np.log(x_var+0.05)-np.log(x_var)], yerr=[-np.log(y_var-1)+np.log(y_var), np.log(y_var+1)-np.log(y_var)], color="black", ecolor='black', capsize=1, label="Data Points")
x_fit = np.linspace(min(np.log(x_var)), max(np.log(x_var)), 1000)
y_fit = mxc(out.beta, x_fit)
plt.plot(x_fit, y_fit, label='Theo Fit')
plt.xlabel('Log(Distance)')
plt.ylabel('Log(Weight added)')
plt.legend()
plt.show()

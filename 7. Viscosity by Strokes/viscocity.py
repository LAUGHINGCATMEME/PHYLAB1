import numpy as np

radius = np.array([4.77, 4.79, 4.79, 4.76, 4.77]) * 10**-3 / 2
radius_err = np.std(radius)
radius = np.mean(radius)
density_sphere = 4860
density_sphere_err = 0.5
density_liquid = 960
density_liquid_err = 0.005 * 10**-3 * 10**6
column_length = 0.100
column_length_err = 0.0005
g = 9.8
g_err = 0.01

tt1 = np.array([1.66, 1.61, 1.6, 1.7, 1.69, 1.73])
tt2 = np.array([1.57, 1.63, 1.65])
tt3 = np.array([1.62, 1.67, 1.6, 1.71, 1.71])


def percent_errr(value, value_err):
    return value_err * 100 / value


print(2 * radius ** 2 * (density_sphere - density_liquid) * g / (9 * column_length/np.mean(tt2)))
v = np.mean(2 * radius ** 2 * (density_sphere - density_liquid) * g / (9 * column_length / tt1))
verr = np.std(2 * radius ** 2 * (density_sphere - density_liquid) * g / (9 * column_length / tt1))
print(v, verr, verr/v*100)
v = np.mean(2 * radius ** 2 * (density_sphere - density_liquid) * g / (9 * column_length / tt2))
verr = np.std(2 * radius ** 2 * (density_sphere - density_liquid) * g / (9 * column_length / tt2))
print(v, verr, verr/v*100)
v = np.mean(2 * radius ** 2 * (density_sphere - density_liquid) * g / (9 * column_length / tt3))
verr = np.std(2 * radius ** 2 * (density_sphere - density_liquid) * g / (9 * column_length / tt3))
print(v, verr, verr/v*100)





print(f""" Time Taken
{np.mean(tt1):.2f} ± {np.std(tt1):.2f}           {np.std(tt1)*100/np.mean(tt1):.2f}
{np.mean(tt2):.2f} ± {np.std(tt2):.2f}           {np.std(tt2)*100/np.mean(tt2):.2f}
{np.mean(tt3):.2f} ± {np.std(tt3):.2f}           {np.std(tt3)*100/np.mean(tt3):.2f}""", end="")

Time_Taken = np.mean(np.hstack((tt1, tt2, tt3)))
Time_Taken_err = np.std(np.hstack((tt1, tt2, tt3)))
Velocity = column_length/Time_Taken
Velocity_err = Velocity * ((Time_Taken_err/Time_Taken) + (column_length_err/column_length))


eta = 2 * radius ** 2 * (density_sphere - density_liquid) * g / (9 * Velocity)
eta_err = eta * ((2*radius_err/radius)**2 + ((density_liquid_err + density_sphere_err)/(density_sphere + density_liquid))**2 + (g_err/g)**2 + (Velocity_err/Velocity)**2)**0.5

print(f"""
Final res: {Time_Taken:.3f} ± {Time_Taken_err:.3f}     {Time_Taken_err*100/Time_Taken:.2f}

eta: {eta} ± {eta_err}   {eta_err*100/eta}% error



{"Radius=":15s} {str(radius):17s} ± {radius_err}                 {percent_errr(radius, radius_err)}
density_sphere = {density_sphere} ± {density_sphere_err}         {percent_errr(density_sphere, density_sphere_err)}
density_liquid = {density_liquid} ± {density_liquid_err}          {percent_errr(density_liquid, density_liquid_err)}
column_length = {column_length} ± {column_length_err}            {percent_errr(column_length, column_length_err)}
g = {g} ± {g_err}                                                 {percent_errr(g, g_err)}
time taken = {Time_Taken} +- {Time_Taken_err} {percent_errr(Time_Taken, Time_Taken_err)}
velocity = {Velocity} += {Velocity_err}  {percent_errr(Velocity, Velocity_err)}

""")






import numpy as np


frequency = np.repeat(np.arange(1, 6), 3)  # Frequency in Khz , number of times
final_distance = np.array([691, 707, 386, 702, 509, 548, 484, 585, 655, 478, 521, 597, 420, 382, 383])  # 509/4
initial_distance = np.array([339, 354, 31, 81.5, 60, 105.5, 72, 55, 67, 39, 83, 71, 68, 31, 32])
number_of_nodes = np.array([2, 2, 2, 7, 5, 5, 7, 9, 10, 10, 10, 12, 10, 10, 10])  # Number of nodes smh

speed_of_sound = np.round((final_distance-initial_distance)*2*frequency/number_of_nodes, decimals=2)

print(np.reshape(speed_of_sound, (5, 3)))

print(f"speed of sound is: {np.mean(speed_of_sound):.2f} +- {np.std(speed_of_sound):.2f} m/sec     {np.std(speed_of_sound)/np.mean(speed_of_sound)*100:.2f}%")
print(f"speed of sound by weighted average is: {np.average(speed_of_sound, weights=final_distance-initial_distance):.2f} +- {np.sqrt(np.cov(speed_of_sound, aweights=final_distance-initial_distance)):.2f} m/sec     {np.sqrt(np.cov(speed_of_sound, aweights=final_distance-initial_distance))/np.average(speed_of_sound, weights=final_distance-initial_distance)*100:.2f}%")
exit()


print(f"speed of sound is: {np.mean(np.delete(speed_of_sound, 4)):.2f} +- {np.std(np.delete(speed_of_sound, 4)):.2f} m/sec     {np.std(np.delete(speed_of_sound, 4))/np.mean(np.delete(speed_of_sound, 4))*100:.2f}%")
np.delete(final_distance, 4)

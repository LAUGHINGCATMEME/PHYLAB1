while True:
    # For plotting the graphs
    dataset = int(input("> "))
    df = pd.read_excel(r"C:\Users\Lenovo\Desktop\phy proj data.xlsx")
    t_values = df.iloc[:, dataset*2-2]  # 3rd column (index 2)
    x_values = df.iloc[:, dataset*2-1]
    """    minima_indices = (np.diff(np.sign(np.diff(x_values))) > 0).nonzero()[0] + 1
    maxima_indices = (np.diff(np.sign(np.diff(x_values))) < 0).nonzero()[0] + 1
    minima_times = [t_values[i] for i in minima_indices]
    minima_values = [x_values[i] for i in minima_indices]
    maxima_times = [t_values[i] for i in maxima_indices]
    maxima_values = [x_values[i] for i in maxima_indices]
    extrema_times = minima_times + maxima_times
    extrema_values = minima_values + maxima_values
    extrema_values = [abs(value) for value in extrema_values]
    extrema_times.sort()
    extrema_values.sort(reverse=True)
    x_values = extrema_values
    t_values = extrema_times"""
    plt.plot(t_values, x_values, marker='o', linestyle='-')
    plt.title(f'Plot of x vs. t on {dataset} data set')
    plt.xlabel('t')
    plt.ylabel('x')
    plt.grid(True)
    plt.show()
exit()



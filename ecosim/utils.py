import matplotlib.pyplot as plt

def plot_simulation(data, title):
    plt.figure(figsize=(10, 5))
    for key, values in data.items():
        plt.plot(values, label=key)
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title(title)
    plt.legend()
    return plt
import matplotlib.pyplot as plt

def plot_bar_chart(labels, values, title='ЛР 3', xlabel='x', ylabel='y'):
    sorted_indices = sorted(range(len(values)), key=lambda i: values[i])

    plt.barh(labels, values, color='skyblue')


    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.grid(axis='x', linestyle='--', alpha=0.7)

    plt.show()

if __name__ == "__main__":
    labels = ['0', '1', '2', '3', '4']
    values = [4, 1, 8, 3, 7]

    plot_bar_chart(labels, values)

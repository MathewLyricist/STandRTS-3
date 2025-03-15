import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3 * np.pi, 3 * np.pi, 1000)

y = np.sin(3 * x) * np.cos(2 * x) / (3 * x)
y[~np.isfinite(y)] = 0

plt.plot(x, y, color='green')

plt.title('График функции y = sin(3x) * cos(2x) / (3x)')
plt.xlabel('x')
plt.ylabel('y')

plt.xticks(np.arange(-3 * np.pi, 4 * np.pi, np.pi),
           [f"{int(k)}π" if k != 0 else "0" for k in np.arange(-3, 4, 1)])

plt.grid()

plt.show()

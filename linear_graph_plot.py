import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 100)
sin_x = np.sin(x)

plt.plot(x, sin_x)
plt.title("Синусоида")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.show()
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)
plt.figure(2)
plt.scatter(x, y, marker='o')
plt.show()
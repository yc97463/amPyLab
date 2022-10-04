import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi)
threshold = 0
y = []
for v in x: # v as value
  if v >= threshold:
    y.append(v)
  else:
    y.append(0)
plt.figure()
plt.scatter(x, y, marker='o')
plt.show()

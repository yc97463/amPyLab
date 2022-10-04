import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi)
threshold = 0
y = []
threshold_high = 1
threshold_low = 0
for v in x: # v as value
  if v >= threshold_high:
    y.append(1)
  elif v <= threshold_low:
    y.append(0)
  else:
    y.append(v)
plt.figure()
plt.scatter(x, y, marker='o')
plt.show()

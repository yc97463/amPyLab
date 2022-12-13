import numpy as np
import matplotlib.pyplot as plt
x_list = []
y_list = []
for line in open("data.txt"):
    ss = line.strip()
    if len(ss) == 0:
        continue
    x, y = ss.split(",")
    x_list.append(float(x))
    y_list.append(float(y))
print(x_list, y_list)
plt.scatter(x_list, y_list, marker='o')
plt.show()

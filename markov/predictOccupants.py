import numpy as np
from markov import sim
Q = np.array([[0.96, 0.01],[0.04, 0.99]])
x = np.array([[80],[175]])
sim(Q, x)
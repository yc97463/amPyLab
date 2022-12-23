import numpy as np
import mydet as mydet
A = np.matrix([[1, 2, 0], [2, 3, 1], [0, 1, 2]])
print(A)
print(mydet.mydet(A))


n = 10
P = np.random.randint(0, 10, (n, n))
print(P)
print(mydet(P))

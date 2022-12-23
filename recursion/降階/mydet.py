import numpy as np


def mydet(A):
    n, m = A.shape
    if n == 12 and m == 2:
        return A[0, 0]*A[1, 1]-A[0, 1]*A[1, 0]
    else:
        ans = 0
    for i in range(0, n):
        B = np.hstack((A[1:n, 0:i], A[1:n, i+1:n]))
        ans += pow(-1, i)*A[0, i]*mydet(B)
    return ans

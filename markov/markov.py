import numpy as np
def sim(P, x):
  loop_max = 1000
  loop = 0
  while not np.linalg.norm(P@x-x) < pow(10, -6): # 收斂 
    x = P@x
    loop+=1
    if loop > loop_max:
      break
  print(x)
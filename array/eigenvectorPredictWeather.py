from tokenize import _all_string_prefixes
import numpy as np
P=np.array([[0.6,0.13],[0.4,0.87]])
value,vector=np.linalg.eig(P)
print(value, vector[:,1],sep='\n')

a,b=abs(vector[:,1])
r=b/(a+b)
print(r)
P@np.array([[1-r],[r]])
print(np.array([[1-r],[r]]))

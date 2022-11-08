import numpy as np
# from np.linalg import inv 

n=9
p=np.array([range(1,n*n+1)])
b=np.reshape(p,(n,n))

a=b[3:8,2:7]
b=a+3*np.eye(5)
c=np.linalg.inv(b)
# d=c@b
d=c.dot(b)
e=d-np.eye(5)

print(a,b,c,d,e,sep='\n========================================\n')
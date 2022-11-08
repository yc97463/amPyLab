import numpy as np

A=np.matrix([[2,1],[1,1],[3,1],[0,1]])
b=np.matrix([[1.95],[-0.48],[4.53],[-2.95]])
AT=np.transpose(A)
B=AT@A
invB=np.linalg.inv(B)
ans=invB@AT@b

print(ans,np.mean(np.abs(A@ans-b)),A@ans,sep='\n')
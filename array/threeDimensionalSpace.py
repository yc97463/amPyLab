import numpy as np
A=np.matrix([[2,5,1],[1,1,1],[3,1,1]])
d=np.matrix([[9],[0],[2]])
print(A,d,sep='\n')
invA = np.linalg.inv(A)
ans=invA@d
print(ans,np.sum(np.abs(A@ans-d)),sep='\n')
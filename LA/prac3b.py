# check if matrix is invertable and if yes then find inverse of matrix 
import numpy as np
m =np.array([[1,2,1] ,[2,1,0],[3,0,2]])
c = np.linalg.det(m)
print("Determinant " , c)
if (c!=0):
    minv = np.linalg.inv(m)
    print("Inverse of matrix ",minv)
else:
    print("Matrix is not invertible ")
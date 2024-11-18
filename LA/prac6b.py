import numpy as np
A=np.asmatrix("2 0 0;0 3 4;0 4 9")
print("A\n",A)
print("Eigenvalues",np.linalg.eigvals(A))
eigenvalues,eigenvectors=np.linalg.eig(A)
print("first tuple of eig",eigenvalues)
print("seconf tuple of eig\n",eigenvectors)
for i in range(len(eigenvalues)):
    print("left",np.dot(A,eigenvectors[:,i]))
    print(...)
778 
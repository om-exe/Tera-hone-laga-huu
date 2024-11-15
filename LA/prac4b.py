# write a program to find rank of a matrix
import numpy as np
my_matrix = np.array([[1,2,1],[3,4,7],[3,6,3]])
print("Matrix ")
for row in my_matrix:
    rank=np.linalg.matrix_rank(my_matrix)
print("Rank is ",rank)
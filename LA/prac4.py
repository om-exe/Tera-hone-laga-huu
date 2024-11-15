#  Write a program to convert a matrix into its row echelon form
from sympy import *
M = Matrix([[1,0,1,3],[2,3,4,7],[-1,-3,-3,-4]])
print("Matrix : {}".format(M))
M_rref=M.rref()
print("The Row echelon form of matrix m amd the pivot coloumn :{} ".format(M_rref))
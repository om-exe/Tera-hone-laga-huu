# Write a program to do the foll
# a enter a vector u as a list 
# enter another vector b as  alist
# find the vector au+bv for different values of a and b
# find the dot product of u and b
import numpy as np
u=np.array([3,4,5])
v=np.array([1,2,3])
print("VEctor u",u)
print("Vector v ",v)
a= int(input("Enter the value of a "))
b= int(input("Enter the value of b "))
print(a*u)    #Extra 
print(v*b)    #Extra 
print("For dot product ",u*v)    #Extra
d = a*u+b*v    #Extra 
p=np.dot(u,v)
print("Vector au+bv ",d)
print("Dot product of u and v  ",p)


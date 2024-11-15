# Basic matrix operatoion
# 1 adiition sub ,mul,
import numpy as np
m1 = np.array([[1,3,4],[8,5,6]])
m2 = np.array([[8,6,9],[9,0,6]])
print("Add matrix ")
a= np.add(m1,m2)
print(a)
print("Subtract Matrix ")
b = np.subtract(m2,m1)
print(b)
x=np.array([[1,7,5],[4,5,3],[3,2,1]])
y=np.array([[6,7,7],[2,3,1],[2,2,3]])
t=np.array([[0,0,0],[0,0,0],[0,0,0]])
print("multiplication ")
for i in range (len(x)):
    for j in range (len(y[0])):
        for k in range (len(y)):
            t[i][j]+=x[i][k]*y[k][j]
for r in t:
    print(r)


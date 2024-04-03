n=int(input("enter the number of rows:"))
m=int(input("enter the number of columns:"))
matrix=[]
print("enter value in matrix:")
for i in range(n):
     data=[ ]
     for j in range(m):
         data.append(int(input()))
     matrix.append(data)
for i in range(n):
    for j in range(m):
           print(matrix[i][j],end=" ")
    print()

for i in range(n):
    sum=0
    for j in range (m):
        sum=sum + matrix[j][i]
        print('sum of row',i+1,':',sum)
for i in range(m):
    sum=0
    for j in range(n):
        sum=sum+matrix[j][i]
        print('sum of column',i,':',sum)
        

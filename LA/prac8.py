rows=int(input("enter number of rows"))
column=int(input("enter number of columns:"))
m=[]
for i in range (rows):
    m.append([])
    for j in range(column):
        e = int(input("enter element:"))
        m[i].append(e)
def scal(m):
    a=int(input('enter value of a:'))
    unew=[]
    for i in range(rows):
        unew.append([])
        for j in range(column):
            unew[i].append([m[i] [j]*a])
    for i in range(rows):
        print(unew[i])
def tran(m):
    rmatrix=[]
    rmatrix=[[0]*rows for i in range(column)];
    for i in range(len(m)):
        for j in range(len(m[0])):
            rmatrix[j][i] = m[i][j]
    for r in rmatrix:
        print(r)
def dis(m):
    for i in range (rows):
        print("row",[i])
        print(m[i])
    for i in range (len(m[0])):
            print("column",[i])
            for j in range(len(m)):
                print("[",m[j][i],"]")
ch=True
while ch:
    print("\n1.dispaly matrix\n2.display row and column\n3.scalar multiplication\n4.transpose of matrix\n5.exit\n")
    ch=int(input("enter choice:"))
    if ch==1:
        for i in range(rows):
            print(m[i])
    elif ch==2:
        dis(m)
    elif ch==3:
         scal(m)
    elif ch==4:
        tran(m)
    elif ch==5:
         print("exit")
         ch=False
    else:
        print("\ninvalid choice")
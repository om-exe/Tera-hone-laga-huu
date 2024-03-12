# Write a program for demonstrate different types of exceptional handling
# A) write program to print the reciprocal of even numbers
try:
    num=int(input("Enter a number: "))
    assert num%2==0
except:
    print("Not an even number")
else:
    reciprocal=1/num
    print(reciprocal)

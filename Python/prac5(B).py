# program to except two numbers from user & perform the div
try :
    print("try block")
    x=int(input("Enter 1st Number: "))
    y=int(input("Enter 2st Number: "))
    z=x/y
except ZeroDivisionError:
    print("Except ZeroDivisionError error block")
    print("Division by 0 not accepted")
else:
    print("else block")
    print("Divison",2)
finally:
    print("Finally block")
    x=0
    y=0
print("Out of try , except , else , Finally blocks")

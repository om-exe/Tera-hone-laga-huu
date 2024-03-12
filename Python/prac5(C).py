try :
    num=int(input("Enter a number upto 50 : "))
    if num>50:
        raise ValueError(num)
except ValueError:
    print(num,"It is out of range ")
else:
    print(num,"It is within the range") 
       

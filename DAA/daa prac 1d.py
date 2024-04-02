def countingevenodd(arr,arr_size):
    even_count =0
    odd_count =0
    for i in range (arr_size):
        if (arr[i] & 1 == 1):
            odd_count +=1
        else:
            even_count +=1
    print("number of even elements=",even_count)
    print("number of even elements=",odd_count)


arr=[2,3,4,5,6,7,8,9,10,11,12,13]
n=len(arr)
countingevenodd(arr,n)
        

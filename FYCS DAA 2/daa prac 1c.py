def getMin(arr,n):
    res=arr[0]
    for i in range (1,n):
        res=max(res,arr[i])
        return res
# maximum function
def getMax(arr,n):
    res=arr[0]
    for i in range(1,n):
        res=max(res,arr[i])
    return res
# driven program
arr=[ 12,1234,45,67,1]
n=len(arr)
print("minimum element of array:",getMin(arr,n))
print("maximum element of array:",getMin(arr,n))

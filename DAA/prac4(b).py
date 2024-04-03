def BinarySearch(array,target):
    # swapped = False
    right,left=0,len(array)
    while right<=left:
        mid = right+left//2
    if target==array(mid):
        return mid
    elif array[mid]<target:
         left = mid+1
    else:
        right = mid+1
a = [12,56,4,57,95,5,28]
BinarySearch(a,4)
print(a)

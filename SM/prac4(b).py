# def BinarySearch(array,target):
#     left=0
#     right=len(array)-1 
#     while left<=right:
#         mid = (left+right)//2
#         if array[mid]==target:
#                 return mid
#         elif array[mid]<target:
#                 left = mid+1
#         else:
#                 right = mid-1
#         return -1
# array = [12,56,4,57,95,5,28]
# BinarySearch(array,4)
# print(array)
# def BinraySearch(array,t):
#       left , right= 0,len(array)-1
#       while left<=right:
#             mid = left+right//2
#             if array[mid]==t:
#                   return t
#             elif array[mid]<t:
#                   left = mid +1
#             else:
#                   right = mid-1
#             return -1
# arr= [1,6,8,2]
# BinraySearch(arr,8)
# print(arr)
# def bs(arr,h):
#       left,right=0,len(arr)-1
#       while left<=right:
#             mid = left+right//2
#             if  arr[mid]==h:
#                   return h
#             elif arr[mid]<h:
#                   right = mid+1
#             else:
#                    left = mid-1;
#             return -1
# arr = [1,56,2,3]
# bs(arr,3)
# print(arr)
                  


def Bin(arr,tar):
    left,right=0,len(arr)-1
    while left<=right:
        mid = left+right//2
        if arr[mid]==tar:
            return tar
        elif arr[mid]<tar:
            left = mid+1
        else:
            right = mid-1
arr = [12,5,6,7]
Bin(arr,7)
print(arr)
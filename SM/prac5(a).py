# def bubble(arr1):
#     n = len(arr1)
#     for i in range(len(arr1)):
#         swapped = False
#         for j in range(0,n-i-1):
#             if arr1[j]>arr1[j+1]:
#                 arr1[j],arr1[j+1]=arr1[j+1],arr1[j]
#                 swapped = True
#         if not swapped:
#             break
# a = [12,56,4,57,95,5,28]
# (bubble(a))
# print(a)










def bub(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
a = [45,5,6,9]
bub(a)
print(a)
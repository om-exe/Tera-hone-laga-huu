def selection(arr):
    n = len(arr)
    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini = j  
                arr[i],arr[mini]=arr[mini],arr[i]
a = [12,56,4,57,95,5,28]
selection(a)
print(a)

        
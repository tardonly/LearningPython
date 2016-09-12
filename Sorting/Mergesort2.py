def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r- q
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0 , n1):
            L[i] = arr[p + i]
    for j in range(0 , n2):
        R[j] = arr[q + 1 + j]
    i = 0    
    j = 0    
    k = p
    while i < n1 and j < n2 :
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr,p,r):
    if p < r:
        q = (p+(r-1))/2
        mergeSort(arr, p, q)
        mergeSort(arr, q+1, r)
        merge(arr, p, q, r)



arr = map(int,raw_input().split())
n = len(arr)
mergeSort(arr,0,n-1)
for i in range(n):
    print ("%d" %arr[i]),



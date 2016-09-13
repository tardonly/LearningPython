def partition(arr,p,r):
    i = ( p-1 )        
    x = arr[r]    
    for j in range(p , r):
        if arr[j] <= x:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[r] = arr[r],arr[i+1]
    return ( i+1 )

def quickSort(arr,p,r):
    if p < r:
        q = partition(arr,p,r)
        quickSort(arr, p, q-1)
        quickSort(arr, q+1, r)


arr = map(int,raw_input().split())
n = len(arr)
quickSort(arr,0,n-1)
for i in range(n):
    print ("%d" %arr[i]),



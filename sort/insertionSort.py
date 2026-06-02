def insertionSort(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j = i - 1
        while ( j>= 0 and a[j] > key):
            a[j+1]=a[j]
            j = j-1
        a[j+1] = key
    print(a)
    



    

arr = [65,34,78,99,12,43,78,23]
insertionSort(arr)

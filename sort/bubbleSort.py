def bubbleSort(a):
    n = len(a)

    for i in range(n):
        for j in range(n-1-i):
            if (a[j]>a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]

    print(a)


arr = [65,34,78,99,12,43,78,23]
bubbleSort(arr)
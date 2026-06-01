def bubbleSort(a):
    n = len(a)

    for i in range(n):
        for j in range(n-1-i):
            if (a[j]>a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]

    print(a)

def deBubbleSort(a):
    n = len(a)

    for i in range(n):
        for j in range(n-1,i,-1):
            if (a[j]>a[j-1]):
                a[j],a[j-1] = a[j-1],a[j]

    print(a)



arr = [65,34,78,99,12,43,78,23]
deBubbleSort(arr)
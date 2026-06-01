def selectionSort(arr):
    size = len(arr)

    for i in range(size):
        min = i
        for j in range(i,size):
            if(arr[min]>arr[j]):
                min = j
        arr[i],arr[min]=arr[min],arr[i]
    

def DeSelectionSort(arr):
    size = len(arr)

    for i in range(size):
        max = i
        for j in range(i,size):
            if(arr[max]<arr[j]):
                max = j
        arr[i],arr[max]=arr[max],arr[i]
    


    
a = [54,44,23,74,676,86,34]

# selectionSort(a)
# print(a)
DeSelectionSort(a)
print(a)


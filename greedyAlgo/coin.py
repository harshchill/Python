def minimumCoin(arr,target):
    arr.sort()
    n = len(arr)
    amount = target
    i = n-1
    while( amount != 0):
        while(arr[i]<=amount):
            amount = amount - arr[i]
            print(arr[i],end="-->")
        i = i-1



  
arr=[500,20,5,1,2,10,50]
minimumCoin(arr,1024)
def findMinMax(arr,start , end):
    if( start == end):
        return arr[start],arr[end]
    if(start+1 == end):
        if(arr[start]<arr[end]):
            return arr[start],arr[end]
        else:
            return arr[end],arr[start]
    
    mid = (start + end )//2

    min1,max1=findMinMax(arr,start,mid)
    min2,max2=findMinMax(arr,mid+1,end)

    return min(min1,min2),max(max1,max2)

arr = [65,34,78,99,12,43,78,23]

min , max = findMinMax(arr,0,len(arr)-1)

print("the minimun valuse is : ",min)
print("the maximum valuse is : ",max)
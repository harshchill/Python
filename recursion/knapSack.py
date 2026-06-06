def knapSack(weight,price,capacity,length):
    if length == 0 or capacity == 0:
        return 0
    if weight[length-1] > capacity:
       return knapSack(weight,price,capacity,length-1)
    include = price[length-1] + knapSack(weight,price,capacity - weight[length-1],length-1)
    exclude = knapSack(weight,price,capacity,length-1)

    return max(include,exclude)

wt=[2,5,5,6]
pr=[14,20,15,12]
cap= 10

print(knapSack(wt,pr,cap,len(wt)))    
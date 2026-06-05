def knapSack(price,weight,capacity):
    n = len(price)
    items = [[price[i],weight[i],price[i]/weight[i]] for i in range(n)]
    profit = 0.0

    for i in range(n):
        for j in range(i+1,n):
            if(items[i][2]<items[j][2]):
                items[i],items[j]=items[j],items[i]
            
    for pr ,wt ,ratio in items:
        if capacity >= wt:
            capacity -= wt
            profit += pr
        else:
            profit = profit + ratio * capacity
            break

    print("maximum profit is : ",profit)


pr=[23,45,67,89,200]
wt=[2,6,3,5,7]
cap=10

knapSack(pr,wt,cap)
            
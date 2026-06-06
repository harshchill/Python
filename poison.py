def findPoisonedDuration(timeSeries, duration):
        if(duration == 0):
             print(0)
             return 0
        allSec =[]
        actual =[]
        for i in timeSeries:
            for j in range(duration):
                allSec.append(i+j)
        for x in allSec:
            if x not in actual:
                actual.append(x)
        print(allSec)
        print(actual)
        return len(actual)

ts = [1,2,3,1,9]
findPoisonedDuration(ts,2)
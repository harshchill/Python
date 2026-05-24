def isArmstrongNumber(val):
    # 153
    target = val
    power = len(str(val))
    total = 0
    
    while val > 0:
        x = val % 10
        total += x**power
        val = val//10

    if(total == target):
        print("Armstrong")
    else:
        print("Nah bro")
        

isArmstrongNumber(153)
isArmstrongNumber(9926315)
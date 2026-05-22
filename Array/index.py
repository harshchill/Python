import array as ar
# from array import * 
# import everything from the array mmodule so we can use it without using alias

# arr = array("i",(1,2,3,4,5,6))
arr = ar.array("i",(1,2,3,4,5,6))

print(arr)

for x in arr:
    print(x , end=" ")

for i in range(0,6) :
    print(arr[i])
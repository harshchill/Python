def findLeaders(arr): 
    
      x = len(arr)
      list =[]
      for i in range(0,x):
          if(arr[i]>arr[i+1]):
              for y in range(i,x):
                  if(arr[i]>arr[y]):
                      list.append(arr[i])
                      
        
      print(list)  

findLeaders([16,17,4,3,5,2])
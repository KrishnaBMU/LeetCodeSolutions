def findWater(arr, n):
    result = 0
    left_max = 0
    right_max = 0
    lo = 0
    hi = n-1
      
    while(lo <= hi):
     
        if(arr[lo] < arr[hi]):
         
            if(arr[lo] > left_max):
 
                left_max = arr[lo]
            else:
                result += left_max - arr[lo]
            lo+= 1
         
        else:
         
            if(arr[hi] > right_max):
                right_max = arr[hi]
            else:
                result += right_max - arr[hi]
            hi-= 1
         
    return result
  
 
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)
 
print("Maximum water that can be accumulated is ",
        findWater(arr, n))
 
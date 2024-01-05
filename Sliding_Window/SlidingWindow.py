# It is a technique that aims to reduce the use of nested loops to a single loop

# arr  = [2,9,31,-4,21,7] ; k =3
# The below code is done using sliding window, max sum in the array this is from youtube channel tap academy "https://youtu.be/jhW7VwP2Djw"

def slidingWindow (arr,k):
    n = len(arr)
    if k > n :
        return 0
    suM = 0
    
    for i in range (k):
        suM += arr[i]
    maX = suM
    
    for i in range  (1,n-k +1):
        suM = suM - arr[i-1] + arr[i+k -1]
        
        if suM > maX :
            maX = suM
    return maX
    

print(slidingWindow([2,9,31,-4,21,7], 3))


 


'''
Find the max Sum sub array of size K 
Input:
N = 4, K = 2
Arr = [100, 200, 300, 400]
Output:
700
Explanation:
Arr3  + Arr4 =700,
which is maximum.

'''

def maxSum(arr,k):
    Sum = Max = 0
    if (k >len(arr)):
        return 0
    
    for i in range (k):
        Sum += arr[i]
    Max = Sum
        
    
    for j in range (1,(len(arr))-k+1):
        Sum  = Sum - arr[j-1] + arr[j+k -1]
        
        if (Sum > Max):
            Max = Sum
            
    return Max



print(maxSum([100,200,300,400],2))



# same problem using while loop
def WhileMax(arr,k):
    Sum =Max =0
    
    if k > len(arr):
        return 0 
    i=0
    while i <k:
        Sum += arr[i]
        i+=1
   
    
    j =1
    while (j <(len(arr)-k +1)):
        Sum = Sum - arr[j-1] + arr[j+k -1]
        j +=1
        
        if (Sum > Max):
            Max = Sum 
    return Max


print (WhileMax([100,200,300,400],2))
'''
Given an array and a positive integer k, find the first negative integer for each and every window(contiguous subarray) of size k.
Print 0 if there is not negative number

Input:
2
5
-8 2 3 -6 10
2
8
12 -1 -7 8 -15 30 16 28
3

Output:
-8 0 -6 -6
-1 -1 -7 -15 -15 0 . 

'''

def firstNegative(arr,k):
    neg = []
    
    while k > len(arr) :
        return 0
    for i in range (k):
        if (arr[i] < 0 ):
            neg.append(arr[i])
        else:
            continue
    for j in range (1, (len(arr))-k +1):
        if arr[j] < 0:
            neg.append(arr[j])
        else:
            neg.append(0)
            
        
        
    
    return neg


# Test Run
print(firstNegative([12,-1,-7,8,-15,30,16,28],3))
    
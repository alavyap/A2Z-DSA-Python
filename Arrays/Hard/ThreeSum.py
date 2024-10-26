'''
Problem Statement: Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero. In short,
you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] such that i!=j, j!=k, k!=i, and their sum is equal to zero.
Example : 
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: Out of all possible unique triplets possible, [-1,-1,2] and [-1,0,1] satisfy the condition of summing up to zero with i!=j!=k
'''
# Brute Force 
def sum3(arr):
    n = len(arr)
    ans = []
    temp = []
    inSet = set()
    for i in range (n):
        for j in range (i+1,n):
            for k in range (j+1,n):
                if arr[i] + arr[j] +arr[k] == 0:
                   temp = [arr[i],arr[j],arr[k]]
                   temp.sort()
                   inSet.add(tuple(temp))
    
    ans = [list(t) for t in inSet]
    for sublist in ans:
        sublist.sort()  # Sort each sublist
    return ans
# Test Run 
# print (sum3( [-1,0,1,2,-1,-4]))


# Better Approach 
def betterSum(arr):
    n = len(arr)
    sumTwo = 0 
    aSet = set()
    for i in range (n):
        store = set()
        # checking for sum 
        for j in range (i+1,n):
            sumTwo = -(arr[i] + arr[j])
            
            if sumTwo in store:
                temp = [arr[i],arr[j],sumTwo]
                temp.sort()
                aSet.add(tuple(temp))
            store.add(arr[j])
    ans = [list(t) for t in aSet]
    for sublist in ans:
        sublist.sort()  # Sort each sublist
    return ans
    
# Test Run 
# print(betterSum([-1,0,1,2,-1,-4]))

# Optimal Approach 
def threeSum(arr):
    arr.sort()
    n = len(arr)
    ans = [] 
    for i in range (n):
        
        # Remove Duplicates
        if i != 0 and arr[i] == arr[i - 1] :
            continue 
        
        # Making 2 Pointers 
        j = i + 1
        k = n - 1 
        
        # condition to check if k cross j 
        while (j < k) :
            tempSum = arr[i] + arr[j] + arr[k] 
            
            # Condition for the increasing the pointers 
            if tempSum < 0:
                j += 1 
                
            elif tempSum > 0 :
                k -= 1 
                
            else : 
                tempArr = [arr[i], arr[j], arr[k]]
                ans.append(tempArr)
                j += 1
                k -= 1
                
                # Skipping Duplicates 
                while (j < k ) and arr[j] == arr[j-1] :
                    j += 1 
                while (j < k ) and arr[k] == arr[k+1] : 
                    k -= 1 
                
    return ans
            
   

# Test Run 
# print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([18,0,30,0,-48,0,-34,-27,-40,-4,-17,-30,-2 ]))
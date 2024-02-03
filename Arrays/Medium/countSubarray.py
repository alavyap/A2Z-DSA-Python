'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/subarray-sums-i_1467103?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
LeetCode :> https://leetcode.com/problems/subarray-sum-equals-k/description/

Problem Statement: Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.
A subarray is a contiguous non-empty sequence of elements within an array.
Example :
Input Format: N = 4, array[] = {3, 1, 2, 4}, k = 6
Result: 2
Explanation: The subarrays that sum up to 6 are [3, 1, 2] and [2, 4].

'''
# Brute Force


from collections import defaultdict



def countSub(arr,s):
    n = len(arr)
    count = 0
    for i in range (n):
        sum  = 0 
        for j in range (i,n):
            sum += arr[j]
            
            if sum == s:
                count += 1
    return count 

# Test Run 
# print(countSub([3,1,2,4],6))

# Optimal Code 
def countSubs(arr,s):
    Sum = 0 
    preSum = 0
    storeSum = {0:1}
    
    for i in arr:
        preSum = preSum + i
        
        if (preSum - s) in storeSum :
            Sum = Sum + storeSum[preSum-s]
            
        if (preSum) not in storeSum:
            storeSum[preSum] = 1
            
        else:
            storeSum[preSum] = storeSum[preSum] + 1
    return Sum

# Test Run 
# print(countSubs([3,1,2,4],6))

def tryA(nums,k):
    '''
    This is same as the longest subarray with positive integers in a continous sequence 
    '''
    n = len(nums)
    mpp = defaultdict(int)
    preSum = 0 
    count = 0 
    
    mpp[0] = 1 
    for i in range (n):
        preSum += nums[i]
        
        remove = preSum -k 
        count += mpp[remove]
        
        mpp[preSum] += 1
    return count 


# Test Run 
print(tryA([3,1,2,4],6))

 
'''
Link :> https://www.codingninjas.com/studio/problems/longest-subarray-with-sum-k_6682399?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM
You are given an array 'a' of size 'n' and an integer 'k'.
Find the length of the longest subarray of 'a' whose sum is equal to 'k'.
Example :
Input: 'n' = 7 'k' = 3
'a' = [1, 2, 3, 1, 1, 1, 1]
Output: 3
Explanation: Subarrays whose sum = '3' are:
[1, 2], [3], [1, 1, 1] and [1, 1, 1]
Here, the length of the longest subarray is 3, which is our final answer.
'''

def longestSubarray(a,k):
    n = len(a)
    max_len = 0 
    sum_dict = {} #dictionary to store prefix sum and its corresponding  index 
    current_sum = 0
    
    for i in range (n):
        current_sum += a[i] 
        
        if current_sum ==k :
            max_len = i+1
            
        if (current_sum -k) in sum_dict :
            max_len = max(max_len, i - sum_dict[current_sum -k])
            
        if current_sum not in sum_dict :
            sum_dict[current_sum] = i 
    
    return max_len

# Test Run 
print(longestSubarray( [1, 2, 3, 1, 1, 1, 1],3))
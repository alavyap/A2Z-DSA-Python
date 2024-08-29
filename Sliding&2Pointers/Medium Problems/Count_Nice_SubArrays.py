'''
LeetCode:> https://leetcode.com/problems/count-number-of-nice-subarrays/description/

Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length


'''


from collections import defaultdict


def numSub(nums,k):
    
    pre_count = defaultdict(int)
    pre_count[0] = 1 
    odd_count = 0 
    ans = 0
    
    for num in nums :
        odd_count += num%2 
        if odd_count - k in pre_count:
            ans += pre_count[odd_count - k]
        pre_count[odd_count ] += 1 
    return ans


a = [1,1,2,1,1]
# a = [2,2,2,1,2,2,1,2,2,2]
k = 3
print(numSub(a,k))
        
        
'''
LeetCode :> https://leetcode.com/problems/subarrays-with-k-different-integers/description/

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length

'''

def subinterger(nums,k):
    n = len(nums)
    mpp = {}
    left = 0 
    dis_count = 0 
    length = 0 
    
    for right in range (n):
        if mpp.get(nums[right], 0) == 0:
            dis_count += 1 
            
        mpp[nums[right]]  = mpp.get(nums[right], 0) + 1
        
        
        while dis_count > k :
            lefty = nums[left]
            mpp[nums[left]] -= 1 
            
            if mpp[nums[left]] == 0 :
                dis_count -= 1 
                del mpp[nums[left]]
            left += 1 
            
        length = max(length, right - left + 1 )
        
    return length


a =  [1,2,1,2,3]
k = 2

print(subinterger(a,k))
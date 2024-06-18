'''
LeetCode :> https://leetcode.com/problems/subsets-ii/


Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example :
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example :
Input: nums = [0]
Output: [[],[0]]
 

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
'''



def subset_with_dup(nums):
    nums.sort()
    n = len(nums)
    res = [] 
    
    def a_backtrack(start,path):
        res.append(path[:])
        
        for i in range (start,n):
            
            if i > start and nums[i] == nums[i-1]:
                continue
            
            path.append(nums[i])
            a_backtrack(i+1,path)
            path.pop()
            
    
    a_backtrack(0,[])
    return res

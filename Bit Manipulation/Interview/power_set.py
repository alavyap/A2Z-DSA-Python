'''
LeetCode :> https://leetcode.com/problems/subsets/description/

Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

# 1 << N can be said as 2 to the power of N
'''

# We can solve this by using backtracking 
# Pseudo Code 
'''
ans = [] 
def back(start,path):
path = [] 
ans.append(path[:])
for i in range (start,len(nums)):
path.append(nums[i])

backtrack(i+1,path)
path.pop() 

backtarck(0,[])
return ans

'''

# Solving Using bit manipulation

def bit_manipulation(m):
    n = len(m)
    s_s = 1 << n 
    ans = [] 
    
    for num in range (s_s):
        li = [] 
        
        for i in range (n):
            if num & (1 << i):
                li.append(m[i])
                
                
        ans.append(li)
        
    return ans


# Test Run 
print(bit_manipulation([1,2,3]))
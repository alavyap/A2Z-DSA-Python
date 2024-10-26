'''
LeetCode :> https://leetcode.com/problems/subsets/description/
GFG :> https://www.geeksforgeeks.org/problems/power-set4302/1

Given an integer array nums of unique elements, return all possible 
subsets(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example :
Input: nums = [1,2,3]
Output: [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]

Example :

Input: nums = [0]
Output: [[],[0]]
'''
# Total Substrings will be 2 ^n , where n is the number of inputs, length of the array


# This is for GFG question :. where the input is a string 
def allPossible(s):
    sub = [] 
    solve(0,s,'',sub)
    sub.sort() 
    return sub
    
    
def solve(i,s, current, sub):
    if (i == len(s)):
        if current :
            sub.append(current)
        return 
    solve (i+1,s,current+ s[i],sub)
    solve (i+1, s, current, sub)




# We need to understand the bit manipulation for solving this question


# LeetCode Solution

def subsets(nums):
    
    def backtrack (start,path):
        res.append(path[:])
        
        for i in range (start, len(nums)):
            path.append(nums[i])
            
            backtrack(i+1, path)
            path.pop()
            
    res = [] 
    backtrack(0,[])
    return res



# Bit Manipulation 
def findSub(nums):
    n = len(nums)
    res = [] 
    for i in range (1 << n):
        subset= [] 
        for j in range (n):
            if i and (1 << j):
                subset.append(nums[j])
            res.append(subset)
    return res


# Iteravtive Approach 
def iterate_sub (nums):
    ans = [[]]
    for num in nums :
        ans += [ curr + [num] for curr in ans]
    return ans
'''
LeetCode :> https://leetcode.com/problems/generate-parentheses/description/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example :
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example :
Input: n = 1
Output: ["()"]
'''

# Recursive Method 
def generateParenthesis(self, n):
    
    result = [] 
    def helper (result, s, left, right):
        if left == 0 and right == 0  :
           result.append(s)
           
        if left > 0  :
            helper(result,s+"(", left-1, right)
        if right > 0 and left < right :
            helper(result,s +")",left,right-1)
              
        
    helper(result,"",n,n)
    return result


# Optimal Approach 

def parenthesis(n):
    
    def recursive(s,left,right):
        if len(s) == 2 *n :
            ans.append(s)
            return 
        
        if left < n :
            recursive(s+'(',left+1,right)
            
        if right < left :
            recursive(s +')',left, right +1 )
            
            
    ans = [] 
    recursive('',0,0)
    return ans

# Time Complexity :. O(2^n) and Space :. O(N)


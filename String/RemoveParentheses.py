'''
Coding Ninja : https://www.naukri.com/code360/problems/maximum-nesting-depth-of-the-parentheses_8144741?leftPanelTabValue=PROBLEM
LeetCode :  https://leetcode.com/problems/remove-outermost-parentheses/description/
Leetcode : A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.
Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.
'''
from collections import deque

def removeOuterParantheses(s):
    stack = deque()
    temp = ""
    arr = []
    
    for i in range (len(s)):
        if s[i] == "(":
            stack.append(s[i])
        else:
            stack.pop()
        
        temp += s[i]
        
        if len(stack) == 0 :
            temp = temp[1:-1]
            arr.append(temp)
            temp = ""
            
    return "".join(arr)
    
    
# Test Run 
# print(removeOuterParantheses("(()())(())"))



'''
Coding Ninja Problem 
'''

def depth(s):
    max_depth = 0 
    current_depth = 0 
    
    for char in s: 
        if char == "(":
            current_depth += 1 
            max_depth = max(max_depth, current_depth)
        elif char == ")":
            current_depth -= 1 
    return max_depth


# Test Run 
print(depth('1+(3*6+(9-3))'))
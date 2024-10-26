'''
LeetCode :> https://leetcode.com/problems/valid-parenthesis-string/description/


Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
 

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.


'''

def checkS (s):
    stack_open = []
    stack_star = [] 
    
    for i,char in enumerate(s):
        if char == "(":
            stack_open.append(i)
        elif char == "*":
            stack_star.append(i)
            
        else :
            if stack_open :
                stack_open.pop()
            elif stack_star :
                stack_star.pop() 
                
            else :
                return False
            
    while stack_open and stack_star :
        if stack_open[-1] > stack_star[-1]:
            return False
        stack_open.pop()
        stack_star.pop()
    
    return len(stack_open) == 0



# Optimal Code 
def sCheck(s):
    start = end = 0 
    
    for char in s :
        if char == "(":
            start +=1 
            end += 1
        elif  char == ")":
            start -= 1 
            end -= 1
        else :
            start -= 1
            end += 1 
        
        if end < 0 :
            return False 
        
        if start < 0 :
            start == 0
          
    return start == 0 


# Test 
s =  "(*))"
print(checkS(s))
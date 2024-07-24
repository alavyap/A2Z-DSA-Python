'''
Leetcode :> https://leetcode.com/problems/valid-parentheses/description/


Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.


'''

from collections import deque


def isV(s):
    
    hold = []
    
    for i in s:
        if (i == "(") or (i == "[") or (i == "{"): 
            hold.append(i)
                
        else : 
            if (len(hold) == 0 ): 
                return False 
              
            ch = hold[-1]
            hold.pop()

            if (i == ")" and ch == "(") or (i == ']' and ch == '[') or (i == '}' and ch == '{'):
                continue
            else :
                return False 
                    
    return (len(hold) == 0 )


# Optimal Approach 

def parm(s):
    
    tack = [] 
    open = "({["
    close = ")}]"
    group = {")":"(", "}":"{", "]":"["}
    
    for i in s :
        if i in open:
            tack.append(i)
        elif i in close :
            if not tack or tack.pop() != group[i] :
                return False 
            
    return len(tack) == 0 
            
    
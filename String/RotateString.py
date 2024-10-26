'''
Coding Ninja :> https://www.naukri.com/code360/problems/check-if-one-string-is-a-rotation-of-another-string_1115683
LeetCode :> https://leetcode.com/problems/rotate-string/description/
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.
Example :
Input: s = "abcde", goal = "cdeab"
Output: true
'''
def rotateString(s,goal):
    n = len(s)
    m = len(goal)
    
    if n != m :
        return False
    
    s_concat = s + s 
    
    if goal in s_concat :
        return True 
    else:
        return False 
    

# Test Run 
s = "abcde"
goal = "cdeab"
print(rotateString(s,goal))

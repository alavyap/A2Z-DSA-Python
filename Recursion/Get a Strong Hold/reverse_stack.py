'''
GFG :> https://www.geeksforgeeks.org/problems/reverse-a-stack/1

You are given a stack St. You have to reverse the stack using recursion.

Example :
Input:
St = {3,2,1,7,6}
Output:
{6,7,1,2,3}
Explanation:
Input stack after reversing will look like the stack in the output.

Your Task:
You don't need to read input or print anything. Your task is to complete the function Reverse() which takes the stack St as input and reverses the given stack.
Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(1)
'''

# Brute Force 
def stack_reverse(St):
    res = St.reverse()
    return res


# Optimal Approach >> Iterative Approach
def reverse(St):
   
    for i in range (len(St) // 2):
        temp  = St[i] 
        St[i] = St[len(St)-i-1]
        St[len(St)-i-1] = temp 
    return St

# Recursive Approach :>> In this we have to use sys to increase the recusrion limit of python interpreter to pass all the test cases 
import sys
sys.setrecursionlimit(2000)

def recursive_stack(St):
    if not St :
        return 
    
    top = St.pop() 
    
    recursive_stack(St)
    stack_reversed(St,top)
    
def stack_reversed(stack,element):
    if not stack :
        stack.append(element)
        return 
    top = stack.pop() 
    stack_reversed(stack,element)
    stack.append(top)
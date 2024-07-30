'''

GFG :> https://www.geeksforgeeks.org/problems/prefix-to-postfix-conversion/1


You are given a string that represents the prefix form of a valid mathematical expression. Convert it to its postfix form.

Example:

Input: 
*-A/BC-/AKL
Output: 
ABC/-AK/L-*
Explanation: 
The above output is its valid postfix form.
Your Task:

Complete the function preToPost(string pre_exp), which takes a prefix string as input and returns its postfix form.

 

Expected Time Complexity: O(N).

Expected Auxiliary Space: O(N).

Constraints:

3<=pre_exp.length()<=100

'''


def preToPost(pre_exp):
    
    aStack = [] 
    
    
    for char in reversed(pre_exp):
        
        if char.isalnum() :
            aStack.append(char)
            
        else :
            operand1 = aStack.pop()
            operand2 = aStack.pop()
            
            final_exp = operand1 + operand2 + char
            aStack.append(final_exp)
            
    return aStack.pop()
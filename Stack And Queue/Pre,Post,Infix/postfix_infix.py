'''

GFG :> https://www.geeksforgeeks.org/problems/postfix-to-infix-conversion/1

You are given a string that represents the postfix form of a valid mathematical expression. Convert it to its infix form.

Example:

Input:
ab*c+ 
Output: 
((a*b)+c)
Explanation: 
The above output is its valid infix form.
Your Task:

Complete the function string postToInfix(string post_exp), which takes a postfix string as input and returns its infix form.

 

Expected Time Complexity: O(N).

Expected Auxiliary Space: O(N).

Constraints:

3<=post_exp.length()<=104

'''


def postToInfix(postFix):
    aStack = [] 
    
    for char in postFix :
        
        if char.isalnum() :
            aStack.append(char)
            
        else :
            operand2 = aStack.pop()
            operand1 = aStack.pop()
            
            final_exp = "(" + operand1 + char + operand2 + ")"

            aStack.append(final_exp)
            
    return aStack.pop()
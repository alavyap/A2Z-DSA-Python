'''
GFG :>  https://www.geeksforgeeks.org/problems/prefix-to-infix-conversion/1


You are given a string S of size N that represents the prefix form of a valid mathematical expression. Convert it to its infix form.

Example 1:

Input: 
*-A/BC-/AKL
Output: 
((A-(B/C))*((A/K)-L))
Explanation: 
The above output is its valid infix form.
Your Task:

Complete the function string preToInfix(string pre_exp), which takes a prefix string as input and return its infix form.

 

Expected Time Complexity: O(N).

Expected Auxiliary Space: O(N).

Constraints:

3<=|S|<=104


'''


def preI(pre_exp):
    
    aStack = [] 
   
    for char in  reversed(pre_exp):
        if char.isalnum() :
           aStack.append(char)
        
        
        else:
            operand1 = aStack.pop()
            operand2 = aStack.pop()
            final_exp = "(" + operand1 + char + operand2 + ")"
            aStack.append(final_exp)
            
    return aStack.pop()
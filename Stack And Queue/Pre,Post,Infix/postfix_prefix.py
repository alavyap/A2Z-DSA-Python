'''
GFG :> https://www.geeksforgeeks.org/problems/postfix-to-prefix-conversion/1




You are given a string that represents the postfix form of a valid mathematical expression. Convert it to its prefix form.

Example 1:

Input: 
ABC/-AK/L-*
Output: 
*-A/BC-/AKL
Explanation: 
The above output is its valid prefix form.

Example 2:

Input: 
ab+
Output: 
+ab
Explanation: 
The above output is its valid prefix form.
Your Task:

Complete the function string postToPre(string post_exp), which takes a postfix string as input and returns its prefix form.

Expected Time Complexity: O(post_exp.length()).

Expected Auxiliary Space: O(post_exp.length()).

Constraints:

3<=post_exp.length()<=16000

'''


def postToPre(post_exp):
    aStack = [] 
    
    for char in post_exp:
        
        if char.isalnum() :
            aStack.append(char) 
            
        else :
            operand2 = aStack.pop() 
            operand1 = aStack.pop()
            
            
            final_exp  = char + operand1 + operand2
            aStack.append(final_exp)
    return aStack.pop()
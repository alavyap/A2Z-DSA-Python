'''
GFG :> https://www.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1

Given an infix expression in the form of string str. Convert this infix expression to postfix expression.

Infix expression: The expression of the form a op b. When an operator is in-between every pair of operands.
Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands.
Note: The order of precedence is: ^ greater than * equals to / greater than + equals to -. Ignore the right associativity of ^.
Example 1:

Input: str = "a+b*(c^d-e)^(f+g*h)-i"
Output: abcd^e-fgh*+^*+i-
Explanation:
After converting the infix expression 
into postfix expression, the resultant 
expression will be abcd^e-fgh*+^*+i-
Example 2:

Input: str = "A*(B+C)/D"
Output: ABC+*D/
Explanation:
After converting the infix expression 
into postfix expression, the resultant 
expression will be ABC+*D/
 
Your Task:
This is a function problem. You only need to complete the function infixToPostfix() that takes a string(Infix Expression) as a parameter and returns a string(postfix expression). The printing is done automatically by the driver code.

Expected Time Complexity: O(|str|).
Expected Auxiliary Space: O(|str|).

Constraints:
1 ≤ |str| ≤ 10^5

'''


def prec(c):
    if c == "^":
        return 3 
    elif c== "/" or c == "*":
        return 2 
    elif c == "+" or c == "-":
        return 1
    else :
        return -1  
        

def convert (s):
    st = [] 
    result = ""
    
    for c in s :
        
        if c.isalnum() :
            result += c 
            
        elif c == "(":
            st.append(c)
        elif  c == ")":
            
            while st and st[-1] != "(":
                result += st.pop() 
            st.pop() 
            
        else :
            while st and prec(c ) <= prec(st[-1]):
                result += st.pop() 
                
            st.append(c) 
            
            
    while st :
        result += st.pop() 
        
    print(result)
    
    
    
# Optimal Code 

def conversion(exp):
    weights =  {"+" : 1, "-":1, "*":2, "/":2, "^":3 }
    result = [] 
    ope = [] 
    
    for char in exp:
        
        if char.isalnum() :
            result.append(char)
            
        elif char == "(":
            ope.append(char)
            
        elif char == ")":
            while ope and ope[-1] != "(":
                result.append(ope.pop())  
            
            if ope and ope[-1] == "(":
                ope.pop() 
                
        else :
            while ope and ope[-1] != "(" and weights.get(char,0) <= weights.get(ope[-1],0):
                result.append(ope.pop())
            ope.append(char)
            
    while ope :
        result.append(ope.pop())
        
    return "".join(result)
                
    
    
    
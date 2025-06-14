'''
Link :> https://leetcode.com/problems/parsing-a-boolean-expression/description/

A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:
't' that evaluates to true.
'f' that evaluates to false.
'!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
'&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
'|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
Given a string expression that represents a boolean expression, return the evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.

Example 1:
Input: expression = "&(|(f))"
Output: false
Explanation: 
First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.

Example 2:
Input: expression = "|(f,f,f,t)"
Output: true
Explanation: The evaluation of (false OR false OR false OR true) is true.

Example 3:
Input: expression = "!(&(f,t))"
Output: true
Explanation: 
First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
Then, evaluate !(f) --> NOT false --> true. We return true.
 

Constraints:

1 <= expression.length <= 2 * 104
expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.
'''

# Memoization
from functools import lru_cache


def evaluate(expression): 
    
    def helper(expr): 
        args = [] 
        start,bal = 0,0
        
        for i,ch in enumerate(expr):
            if ch == "," and bal == 0 : 
                args.append(expr[start:i])
                start = i +1
            elif ch == "(": 
                bal += 1
            elif ch == ")":
                bal -= 1
                
        args.append(expr[start:])
        return args
    
    @lru_cache(None)
    def dp(expr): 
        if expr == "t":
            return True
        if expr == "f":
            return False
        if expr[0] == "!":
            return not dp(expr[2:-1])
        if expr[0] == "&":
            return all(dp(sub) for sub in helper(expr[2:-1]))
        if expr[0] == "|": 
            return any (dp(sub) for sub in helper(expr[2:-1]))
        
        
    return dp(expression)
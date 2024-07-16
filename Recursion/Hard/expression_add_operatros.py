'''
LeetCode :> https://leetcode.com/problems/expression-add-operators/description/


Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

 

Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
Example 3:

Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.
 

Constraints:

1 <= num.length <= 10
num consists of only digits.
-231 <= target <= 231 - 1



'''
def addOperators(nums,target):
    
    L = len(nums)
    ans = set()
    
    def backtrack(i,total,last,expr):
       # This part of the code is checking if we have reached the end of the input string `nums`. If
       # we have reached the end (`i == L`), it then checks if the `total` value calculated so far is
       # equal to the target value. If it is, it adds the current expression `expr` to the set `ans`.
       # This is essentially a base case for the recursive function, ensuring that we only add valid
       # expressions that evaluate to the target value.
        if i == L :
            if total == target: 
                ans.add(expr)
            return 
        
        
        for j in range (i,L):
           # This part of the code is responsible for generating all possible combinations of
           # expressions by inserting the operators '+', '-', and '*' between the digits of the input
           # string `nums`. Here's a breakdown of what each step does:
            n = int(nums[i:j+1])
            
            if i == 0 : 
                backtrack(j+1,n,n,str(n))
            else : 
                backtrack(j+1,total + n ,n, expr + "+" +str(n))
                backtrack(j+1,total - n, -n , expr + "-" + str(n))
                backtrack(j+1,total - last + last *n , last * n, expr + "*" + str(n))
                
                
            if n == 0 :   #checking for the leading zeroes
                break 
    backtrack(0,0,0,"")
    return list(ans)

# Time :. O(4^N∗N)
# Space :. O(N)
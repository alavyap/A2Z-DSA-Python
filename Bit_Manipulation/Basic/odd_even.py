'''
GFG :> https://www.geeksforgeeks.org/problems/odd-or-even3618/1

Given a positive integer N, determine whether it is odd or even.

Example 1:
Input:
N = 1
Output:
odd
Explanation:
The output is self-
explanatory.
 

Example 2:
Input:
N = 2
Output:
even
Explanation:
The output is self-
explanatory.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function oddEven() which takes the integer N and return "even" if number is even and "odd" if the number is odd.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

Constraints:
0 <= N <= 10000

'''


# Brute Force 
def odd_even(n): 
    ans = []
    count = 0 
    
    while n >0 :
        remainder = n % 2
        ans.append(remainder)
        n = n // 2 
       
    for i in range (len(ans)):
        if ans[i] == 1 :
            count += 1 
        else :
            continue
        
    if count ==  1 :
        return True
    else:
        return False
             


# print(odd_even(2))


# Optimal Approach 
def evenand_odd(N):
    if N & 1  :
        return False 
    return True 


print(evenand_odd(6))
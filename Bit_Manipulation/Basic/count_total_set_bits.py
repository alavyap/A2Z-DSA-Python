'''
GFG :> https://www.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1
Coding Ninja :> https://www.naukri.com/code360/problems/count-set-bits_1112627?interviewProblemRedirection=true&search=count&practice_topic%5B%5D=Bit%20Manipulation&leftPanelTabValue=PROBLEMcout

You are given a number N. Find the total count of set bits for all numbers from 1 to N(both inclusive).

Example 1:
Input: N = 4
Output: 5
Explanation:
For numbers from 1 to 4.
For 1: 0 0 1 = 1 set bits
For 2: 0 1 0 = 1 set bits
For 3: 0 1 1 = 2 set bits
For 4: 1 0 0 = 1 set bits
Therefore, the total set bits is 5.

Example 2:
Input: N = 17
Output: 35
Explanation: From numbers 1 to 17(both inclusive), 
the total number of set bits is 35.

Your Task: The task is to complete the function countSetBits() that takes n as a parameter and returns the count of all bits.

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:  
1 ≤ N ≤ 108

'''   

# Brute Force 

def countSet(n):
    ans = []
    count = 0
    
    for i in range (1,n+1):
        helper(i,ans)
    
    for r in (ans):
        for c in r :
            if c == 1 :
                count += 1 
    return count

def helper(num,ans):
    single = [] 
    
    while num > 0 :
        remainder = num % 2 
        single.append(remainder)
        num = num // 2 
        
    ans.append(single)
    return ans 
        
'''
Test Run 
print(countSet(4))

Better Approach
'''

def binary(n):
    count = 0 
    for i in range ( 1, n+1):
        count += bin(i).count('1')
    return count



# print(binary(4))



# For Just counting the set bit for the given number  >><< Optimal Appraoch 
def justN (n):
    count = 0 
    while (n != 0 ):
        n = n & (n-1)
        count += 1 
    return count

# print(justN(13))




# IF we have to find the set bits for 1 to N 

def allBinary(n):
    
    n +=  1 
    count = 0 
    x = 2 
    
    while (x >> 1 ) < n :
        quotient = n // x 
        count += quotient * (x >> 1 )
        remainder = n % x 
        
        if remainder > (x >> 1) :
            count += remainder - (x >> 1)
        x *= 2 
    return count
            
print(allBinary(6))
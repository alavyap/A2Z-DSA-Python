'''
GFG :> https://www.geeksforgeeks.org/problems/set-the-rightmost-unset-bit4436/1

Given a non-negative number n . The problem is to set the rightmost unset bit in the binary representation of n.

Examples :

Input: n = 6
Output: 7
Explanation: The binary representation of 6 is 110. After setting right most bit it becomes 111 which is 7.
Input: n = 15
Output: 31
Explanation: The binary representation of 15 is 01111. After setting right most bit it becomes 11111 which is 31.
Expected Time Complexity: O(Logn)
Expected Auxiliary Space: O(1)


Constraints:
1 <= n <= 109
'''


# Brute Force 
def bit(n):
    ans = [] 
    while n > 0 :
        rem  = n % 2 
        ans.append(rem)
        n = n // 2 
        
    ans.reverse() 
    l = len(ans)
    bit_flag = False 
   
    
    for i in range (l):
        if ans[i] == 0 :
            ans[i] = 1 
            bit_flag = True
            break 
        
        
      # If no 0 was found (all bits are 1), add an extra bit
    if not bit_flag :
        ans.insert(0,1)
        
    # TO convet bits into integer
    result = 0 
    for b in ans :
        result = (result  << 1 ) | b
    return result

# Test Run 
print(bit(49971))


# Optimal Approach

def bit_manipulation(n):
    return n | (n + 1)
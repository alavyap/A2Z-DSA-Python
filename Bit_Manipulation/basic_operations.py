'''
GFG :. https://www.geeksforgeeks.org/problems/bit-manipulation-1666686020/1

Given a 32 bit unsigned integer num and an integer i. Perform following operations on the number - 

1. Get ith bit

2. Set ith bit

3. Clear ith bit

Note : For better understanding, we are starting bits from 1 instead 0. (1-based). You have to print space three space seperated values ( as shown in output ) and do not have to return anything.

Examples :

Input: 70 3
Output: 1 70 66
Explanation: Bit at the 3rd position from LSB is 1. (1 0 0 0 1 1 0) .The value of the given number after setting the 3rd bit is 70. The value of the given number after clearing 3rd bit is 66. (1 0 0 0 0 1 0)
Input: 8 1
Output: 0 9 8
Explanation: Bit at the first position from LSB is 0. (1 0 0 0)  .The value of the given number after setting the 1st bit is 9. (1 0 0 1).  The value of the given number after clearing 1st bit is 8. (1 0 0 0)
 

Constraints:

0<=num<=109
1<=i<=32
'''
# Brute Force 
def bitManipulation(self,num,i) :
    # This is my approach , i am happy that i was able to solve it ,using the basic logic 🙌🙌 that i knew in the past now in this i have learned about shifting and other operators
    ans = [] 
    
    
    # Converting integer to binary 
    while num > 0 :
        remainder = num %2
        ans.append(remainder)
        num = num // 2 
        
    ans.reverse() 
    
    
    # for reversing the ith position 
    position = i 
    
    mask = ~(1 << position)
    
    new_num = num & mask 
    
    
    # Converting binary to interger
    int_ans = 0 
    for bit in ans :
        int_ans = (int_ans << 1) | bit         
    return [ans[i] ,num, int_ans]




# Optimal code 

def main (num,i) :
    ith_bit = get_ith(num,i)
    
    num_set = set_ith(num,i)
    
    num_clear = clear_ith(num,i)

    print(ith_bit,num_set,num_clear)

def get_ith(num,i):
    bit_mask = 1 <<(i-1)
    return (num & bit_mask) >> (i-1)
    
    
def set_ith(num,i):
    bit_mask = 1 << (i -1)
    return num | bit_mask

    
def clear_ith(num,i):
    
    bit_mask = ~(1 << (i-1))
    return num & bit_mask
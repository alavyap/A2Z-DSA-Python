'''
Link :> https://leetcode.com/problems/count-and-say/description/

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.

 

Example 1:

Input: n = 4

Output: "1211"

Explanation:

countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"
Example 2:

Input: n = 1

Output: "1"

Explanation:

This is the base case.
 

Constraints:

1 <= n <= 30
 
Follow up: Could you solve it iteratively?


'''


# Recursive 

def countAndSay(s):
    if s == 1 :
        return "1"
    return rle(countAndSay(s-1))

def rle(n):
    result = []
    count = 1 
    for i in range (1,len(n)):
        if n[i] == n[i-1]:
            count += 1 
        else:
            result.append(f"{count}{n[i-1]}")
            count = 1 
    result.append(f"{count}{n[-1]}")
    return "".join(result)



# Iterative Apporach
def countAndsay(n):
    
    current = "1"
    
    for _ in range (1,n):
        result = [] 
        count = 1 
        
        for i in range (1,len(current)): 
            if current[i] == current[i-1]: 
                count += 1 
            else: 
                result.append(f"{count}{current[i-1]}")
                count = 1 
        result.append(f"{count}{current[-1]}")
        current = "".join(result)
        
    return current

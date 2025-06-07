'''
Link :> https://www.naukri.com/code360/problems/longest-common-substring_1214702

Problem statement
You have been given two strings “str1” and “str2”. You have to find the length of the longest common substring.

A string “s1” is a substring of another string “s2” if “s2” contains the same characters as in “s1”, in the same order and in continuous fashion also.

For example :
If “str1” = “abcjklp” and “str2” = “acjkp”  then the output will be 3.

Explanation : The longest common substring is “cjk” which is of length 3.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 100
1 <= |str1|, |str2| <= 100

where ‘T’ is the number of test cases and |str| is the length of the string str.
Sample Input 1:
2
abcjklp acjkp
wasdijkl wsdjkl
Sample Output 1:
3
3
Sample Input 2:
2
abcy acby
tyfg cvbnuty
Sample Output 2:
1
2
Explanation: The longest common substrings in first test case are “a”, "b", "c", “y” all having length 1.
'''

# Tabulation 

def LCSubstring(s1,s2):
    n = len(s1)
    m = len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    ans = 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                val = 1 + dp[i - 1][j - 1]
                dp[i][j] = val
                ans = max(ans, val)
            else:                
                dp[i][j] = 0
    return ans



# Space Optimization 
def substringLC(str1,str2): 
    n = len(str)
    m = len(str2)
    
    prev = [0 for i in range(m + 1)]
    cur = [0 for i in range(m + 1)]
    ans = 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str[i-1] == str2[j-1]:
                val = 1 + prev[j-1]
                cur[j] = val
                ans = max(ans, val)
            else:
                cur[j] = 0
        prev = cur[:]
    return ans

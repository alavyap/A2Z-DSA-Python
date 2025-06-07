'''
Link :> https://www.naukri.com/code360/problems/print-longest-common-subsequence_8416383


Problem statement
You are given two strings ‘s1’ and ‘s2’.
Return the longest common subsequence of these strings.
If there’s no such string, return an empty string. If there are multiple possible answers, return any such string.

Note:
Longest common subsequence of string ‘s1’ and ‘s2’ is the longest subsequence of ‘s1’ that is also a subsequence of ‘s2’. A ‘subsequence’ of ‘s1’ is a string that can be formed by deleting one or more (possibly zero) characters from ‘s1’.


Example:
Input: ‘s1’  = “abcab”, ‘s2’ = “cbab”
Output: “bab”
Explanation:
“bab” is one valid longest subsequence present in both strings ‘s1’ , ‘s2’.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
5 6
ababa
cbbcad

Expected Answer:
"bba"
Output on console:
1
Explanation of sample output 1:
“bba” is only possible longest subsequence present in both s1 = “ababa” and s2 = “cbbcad”. '1' is printed if the returned string is equal to "bba". 

Sample Input 2:
3 3
xyz
abc
Expected Answer:
""
Output on console:
1
Explanation of sample output 2:
There’s no subsequence of ‘s1’ that is also present in ‘s2’. Thus an empty string is returned and '1' is printed.


Expected Time Complexity:
Try to solve this in O(n*m). Where ‘n’ is the length of ‘s1’ and ‘m’ is the length of ‘s2’. 


Constraints:
1 <= n, m <= 10^3
Time Limit: 1 sec
'''

def printLCS(n,m,s1,s2): 
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for ind1 in range(1, n + 1):
        for ind2 in range(1, m + 1):
            if s1[ind1 - 1] == s2[ind2 - 1]:
                dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
            else:
                dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

    # Reconstruct LCS
    i, j = n, m
    lcs = []

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))
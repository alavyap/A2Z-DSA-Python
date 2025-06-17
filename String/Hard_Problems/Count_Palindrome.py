'''
Link :> https://www.naukri.com/code360/problems/count-palindromic-subsequences_1062696

Problem statement
A subsequence of a string is achieved by removing some (possibly 0) characters without changing the order of the remaining characters.
You have been given a string 's'.
Find the number of non-empty palindromic subsequences (not necessarily be distinct) in string 's' and return that number modulo 10 ^ 9 + 7.


Example :
Input: 's' = "pqqr"
Output: 5
Explanation: The subsequences are:
p

q

q

r

qq

Please note that both "q" are considered different.
Detailed explanation ( Input/output format, Notes, Images )

Sample Input 1 :
pqqr
Sample output 1 :
5
Explanation of Sample output 1 :
The subsequences are:
p
q
q
r
qq
Please note that both "q" are considered different.


Sample Input 2 :
abc
Sample output 2 :
3

Sample Input 3:
aaaa
Sample Output 3:
15
Expected time complexity :
The expected time complexity is O(|s| ^ 2).


Constraints :
1 <= |s| <= 1000
Where |s| denotes the length of 's'.
Time limit: 1 sec
'''

MOD = 10 ** 9 + 7
def countPalindromic(s):
    n = len(s)
    prev = [0] * n 
    
    for i in range (n -1,-1,-1):
        curr = [0] * n 
        curr[i]  = 1 
        for j in range (i +1,n): 
            if s[i] == s[j] : 
                curr[j] = (prev[j] + curr[j-1] + 1 ) % MOD
            else: 
                curr[j] = (prev[j] + curr[j-1] - prev[j -1]) % MOD 
                if curr[j] < 0: 
                    curr[j] += MOD
                    
        prev = curr 
    return prev[n -1]
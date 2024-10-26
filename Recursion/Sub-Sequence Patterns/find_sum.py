'''

Coding Ninja :> https://www.naukri.com/code360/problems/subset-sum_630213

Problem statement
You are given an array 'A' of 'N' integers. You have to return true if there exists a subset of elements of 'A' that sums up to 'K'. Otherwise, return false.
For Example
'N' = 3, 'K' = 5, 'A' = [1, 2, 3].
Subset [2, 3] has sum equal to 'K'.
So our answer is True.

Detailed explanation ( Input/output format, Notes, Images )
Sample Input  :
4 13
4 3 5 2
Sample Output  :
No
Sample Input 2 :
5 14
4 2 5 6 7
Sample Output 2 :
Yes

Constraints :
1 <= 'N' <= 10^3
1 <= 'A[i]' <= 10^3
1 <= 'K' <= 10^3
Time Limit: 1 sec

'''


def isSubsetPresent(n, k, a ) :
    # Write your code here.
    dp = [1] + [0] * k 

    MOD = 10 ** 9 + 7 


    for num in a :
        for pos in range (k,num -1, -1):
            dp[pos] = (dp[pos] +dp[pos - num]) % MOD 

    if dp[k] > 0 :
        return True 
    return False
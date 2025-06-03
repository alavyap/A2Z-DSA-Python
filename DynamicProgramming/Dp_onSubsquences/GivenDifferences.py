'''

Link :>https://www.naukri.com/code360/problems/partitions-with-given-difference_3751628?source=youtube&campaign=striver_dp_videos 

Given an array ‘ARR’, partition it into two subsets (possibly empty) such that their union is the original array. Let the sum of the elements of these two subsets be ‘S1’ and ‘S2’.

Given a difference ‘D’, count the number of partitions in which ‘S1’ is greater than or equal to ‘S2’ and the difference between ‘S1’ and ‘S2’ is equal to ‘D’. Since the answer may be too large, return it modulo ‘10^9 + 7’.

If ‘Pi_Sj’ denotes the Subset ‘j’ for Partition ‘i’. Then, two partitions P1 and P2 are considered different if:

1) P1_S1 != P2_S1 i.e, at least one of the elements of P1_S1 is different from P2_S2.
2) P1_S1 == P2_S2, but the indices set represented by P1_S1 is not equal to the indices set of P2_S2. Here, the indices set of P1_S1 is formed by taking the indices of the elements from which the subset is formed.
Refer to the example below for clarification.
Note that the sum of the elements of an empty subset is 0.

For example :
If N = 4, D = 3, ARR = {5, 2, 5, 1}
There are only two possible partitions of this array.
Partition 1: {5, 2, 1}, {5}. The subset difference between subset sum is: (5 + 2 + 1) - (5) = 3
Partition 2: {5, 2, 1}, {5}. The subset difference between subset sum is: (5 + 2 + 1) - (5) = 3
These two partitions are different because, in the 1st partition, S1 contains 5 from index 0, and in the 2nd partition, S1 contains 5 from index 2.
Input Format :
The first line contains a single integer ‘T’ denoting the number of test cases, then each test case follows:

The first line of each test case contains two space-separated integers, ‘N’ and ‘D,’ denoting the number of elements in the array and the desired difference.

The following line contains N integers denoting the space-separated integers ‘ARR’.
Output Format :
For each test case, find the number of partitions satisfying the above conditions modulo 10^9 + 7.
Output for each test case will be printed on a separate line.
Note :
You are not required to print anything; it has already been taken care of. Just implement the function.
Constraints :
1 ≤ T ≤ 10
1 ≤ N ≤ 50
0 ≤ D ≤ 2500
0 ≤ ARR[i] ≤ 50

Time limit: 1 sec
Sample Input 1 :
2
4 3
5 2 6 4
4 0
1 1 1 1
Sample Output 1 :
1
6
Explanation For Sample Input 1 :
For test case 1:
We will print 1 because :
There is only one possible partition of this array.
Partition : {6, 4}, {5, 2}. The subset difference between subset sum is: (6 + 4) - (5 + 2) = 3

For test case 2:
We will print 6 because :
The partition {1, 1}, {1, 1} is repeated 6 times:
Partition 1 : {ARR[0], ARR[1]}, {ARR[2], ARR[3]}
Partition 2 : {ARR[0], ARR[2]}, {ARR[1], ARR[3]}
Partition 3 : {ARR[0], ARR[3]}, {ARR[1], ARR[2]}
Partition 4 : {ARR[1], ARR[2]}, {ARR[0], ARR[3]}
Partition 5 : {ARR[1], ARR[3]}, {ARR[0], ARR[2]}
Partition 6 : {ARR[2], ARR[3]}, {ARR[0], ARR[1]}
The difference is in the indices chosen for the subset S1(or S2).
Sample Input 2 :
3
3 1
4 6 3
5 0
3 1 1 2 1
5 1
3 2 2 5 1
Sample Output 2 :
1
6
3


'''

# Memoization 
from ast import Mod


mod = int(1e9 + 7 )
def countPartition(n,d,arr): 
    n = len(arr)
    totalSum = sum(arr)
    
    if totalSum - d < 0 : 
        return 0 
    if (totalSum -d ) % 2 ==1 : 
        return 0 
    s2 = (totalSum -d ) // 2 
    dp = [[-1 for _ in range (s2+1)] for _ in range (n)]
    return helper(n-1,s2,arr,dp)


def helper(ind,target,arr,dp):
    
    if ind == 0: 
        if target == 0 and arr[0] == 0: 
            return 2 
        if target == 0 or target ==arr[0]:
            return 1 
        return 0 
    
    if dp[ind][target] != -1 :
        return dp[ind][target]
    
    notTaken = helper(ind-1,target,arr,dp)
    taken = 0 
    
    if arr[ind] <= target: 
        taken = helper(ind-1,target -arr[ind],arr,dp)
    dp[ind][target] = (notTaken + taken) % mod
    return dp[ind][target]


# Tabulation 
MOD = int(1e9 + 7)
def findDiff(n,d,arr): 
    totalSum = sum(arr)
    
    if (totalSum -d) < 0 or (totalSum -d) % 2: 
        return 0 
    return helper(arr,(totalSum -d) //2 )


def helper(arr,tar): 
    n = len(arr)
    dp = [[0] * (tar + 1) for _ in range (n)]
    
    if arr[0] == 0 : 
        dp[0][0] = 2
    else: 
        dp[0][0] =1 
    
    if arr[0] != 0 and arr[0] <= tar: 
        dp[0][arr[0]] = 1 
        
    for ind in range (1,n): 
        for target in range (tar +1): 
            notTaken = dp[ind -1][target]
            taken = 0 
            if arr[ind] <= target: 
                taken = dp[ind-1][target - arr[ind]]
            dp[ind][target] = (notTaken + taken) % MOD 
    return dp[n-1][tar]


# Space Optimization 

def countPartitions(n,d,arr):
    
    total = 0 
    for i in range (n): 
        total += arr[i] 
        
    if total - d < 0 or (total -d) % 2 : 
        return 0 
    return helper(arr,(total -d) // 2)

def helper(arr,tar): 
    n = len(arr) 
    prev = [0] * (tar + 1 )
    if arr[0] == 0 : 
        prev[0] = 2 
    else: 
        prev[0] = 1
    
    if arr[0] != 0 and arr[0] <= tar: 
        prev[arr[0]] = 1 
    
    for ind in range (1,n): 
        curr = [0]  * (tar +1)
        for target in range (tar +1): 
            notTaken = prev[target]
            
            taken = 0 
            if arr[ind] <= target: 
                taken = prev[target - arr[ind]]
                
            curr[target] = (notTaken + taken) % MOD
        prev = curr 
    return prev[tar]
             
        
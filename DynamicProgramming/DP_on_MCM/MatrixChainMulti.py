'''

Link :> https://www.naukri.com/code360/problems/matrix-chain-multiplication_975344?source=youtube&campaign=striver_dp_videos

Problem statement
Given a chain of matrices A1, A2, A3,.....An. Your task is to find out the minimum cost to multiply these matrices. The cost of matrix multiplication is defined as the number of scalar multiplications. A Chain of matrices A1, A2, A3,.....An is represented by a sequence of numbers in an array ‘arr’ where the dimension of 1st matrix is equal to arr[0] * arr[1] , 2nd matrix is arr[1] * arr[2], and so on.
 
For example:
For arr[ ] = { 10, 20, 30, 40}, matrix A1 = [10 * 20], A2 = [20 * 30], A3 = [30 * 40]

Scalar multiplication of matrix with dimension 10 * 20 is equal to 200.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
2
4
4 5 3 2
4
10 15 20 25
Sample Output 1:
70
8000
Sample Output Explanation 1:
In the first test case, there are three matrices of dimensions A = [4 5], B = [5 3] and C = [3 2]. The most efficient order of multiplication is A * ( B * C).
Cost of ( B * C ) = 5 * 3 * 2 = 30  and (B * C) = [5 2] and A * (B * C) = [ 4 5] * [5 2] = 4 * 5 * 2 = 40. So the overall cost is equal to 30 + 40 =70.

In the second test case, there are two ways to multiply the chain - A1*(A2*A3) or (A1*A2)*A3.

If we multiply in order- A1*(A2*A3), then the number of multiplications required is 11250.

If we multiply in order- (A1*A2)*A3, then the number of multiplications required is 8000.

Thus a minimum number of multiplications required is 8000. 
Sample Input 2:
1
4
1 4 3 2
Sample Output 2:
18
Explanation of Sample Output 2:
In the first test case, there are three matrices of dimensions A = [1 4], B = [4 3] and C = [3 2]. The most efficient order of multiplication is (A *  B) * C .


'''
# Memoization 
import sys


def matrixChain(arr,n): 
    
    dp = [[-1 for _ in range (n)] for _ in range (n)]
    
    def helper(i,j): 
        if i == j : 
            return 0 
        
        if dp[i][j] != -1: 
            return dp[i][j] 
        
        mini = sys.maxsize
        for k in range (i,j): 
            cost = helper(i,k) + helper(k+1,j) + arr[i-1] * arr[k] * arr[j]
            mini = min(mini,cost)
            
        dp[i][j] = mini 
        return mini 
    return helper(1,n-1) 
        
        
# Tabulation 

def matrix(arr,n): 
    
    dp = [[-1 for _ in range (n)] for _ in range (n)]
    
    for i in range (n): 
        dp[i][i] = 0 
        
        
    for i in range (n-1,1,-1): 
        for j in range (i +1,n): 
            mini = float("inf")
            
            for k in range (i,j): 
                ans = dp[i][k] + dp[k+1][j] + arr[i-1] * arr[k] * arr[j] 
                
                mini = min(mini,ans)
            dp[i][j] = mini 
            
    return dp[1][n-1]

    
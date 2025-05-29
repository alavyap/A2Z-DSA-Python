'''
Link :> https://www.naukri.com/code360/problems/ninja-s-training_3621003

Ninja is planing this ‘N’ days-long training schedule. Each day, he can perform any one of these three activities. (Running, Fighting Practice or Learning New Moves). Each activity has some merit points on each day. As Ninja has to improve all his skills, he can’t do the same activity in two consecutive days. Can you help Ninja find out the maximum merit points Ninja can earn?

You are given a 2D array of size N*3 ‘POINTS’ with the points corresponding to each day and activity. Your task is to calculate the maximum number of merit points that Ninja can earn.

For Example
If the given ‘POINTS’ array is [[1,2,5], [3 ,1 ,1] ,[3,3,3] ],the answer will be 11 as 5 + 3 + 3.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 10
1 <= N <= 100000.
1 <= values of POINTS arrays <= 100 .

Time limit: 1 sec
Sample Input 1:
2
3
1 2 5 
3 1 1
3 3 3
3
10 40 70
20 50 80
30 60 90
Sample Output 1:
11
210
Explanation of sample input 1:
For the first test case,
One of the answers can be:
On the first day, Ninja will learn new moves and earn 5 merit points. 
On the second day, Ninja will do running and earn 3 merit points. 
On the third day, Ninja will do fighting and earn 3 merit points. 
The total merit point is 11 which is the maximum. 
Hence, the answer is 11.

For the second test case:
One of the answers can be:
On the first day, Ninja will learn new moves and earn 70 merit points. 
On the second day, Ninja will do fighting and earn 50 merit points. 
On the third day, Ninja will learn new moves and earn 90 merit points. 
The total merit point is 210 which is the maximum. 
Hence, the answer is 210.
Sample Input 2:
2
3
18 11 19
4 13 7
1 8 13
2
10 50 1
5 100 11
Sample Output 2:
45
110
'''


def ninjaT(n,points):
    dp = [[-1 for j in range(4)] for i in range (n)]
    return helper(n-1,3,points,dp)


def helper(day,last,points,dp): 
    
    if dp[day][last] != -1 :
        return dp[day][last] 
    
    if day == 0 : 
        maxi = 0 
        for i in range (3): 
            if i != last: 
                maxi  = max(maxi,points[0][i])
        dp[day][last] = maxi 
        return dp[day][last]
    
    maxi = 0 
    for i in range (3): 
        if i != last: 
            activity = points[day][i] + helper(day-1,i,points,dp)
            maxi = max(maxi,activity)
    dp[day][last] = maxi 
    return dp[day][last]


# Tabulation 

def trainingNinja(n,points): 
    
    dp = [[0 for j in range(4)] for i in range (n)]
    
    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0],points[0][2])
    dp[0][2] = max(points[0][0],points[0][1])
    dp[0][3] =  max(points[0][0], max(points[0][1],points[0][2]))
    
    for day in range (1,n): 
        for last in range (4): 
            dp[day][last] = 0 
            for task in range (3): 
                if task != last: 
                    activity = points[day][task] + dp[day -1][task]
                    dp[day][last] = max(dp[day][last],activity)                    
    return dp[n-1][3]


# Space Optimization
def TrainNinja(n,points):
    prev = [0] *4
    prev[0] = max(points[0][1],points[0][2])
    prev[1] = max(points[0][0],points[0][2])
    prev[2] = max(points[0][0],points[0][1])
    prev[3] = max(points[0][0],max(points[0][1],points[0][2]))
    
    for day in range (1,n):
        
        temp = [0] * 4 
        for last in range (4): 
            temp[last] = 0 
            
            for task in range (3): 
                if task != last: 
                    activity = points[day][task] + prev[task]
                    temp[last] = max(temp[last],activity)
        prev = temp 
    return prev[3] 
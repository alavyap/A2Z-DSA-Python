'''
GFG :> https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1

Given a set of n jobs where each jobi has a deadline and profit associated with it.

Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit associated with a job if and only if the job is completed by its deadline.

Find the number of jobs done and the maximum profit.

Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job. Deadline of the job is the time on or before which job needs to be completed to earn the profit.

Examples :

Input: Jobs = [[1,4,20],[2,1,1],[3,1,40],[4,1,30]]
Output: 2 60
Explanation: Job1 and Job3 can be done with maximum profit of 60 (20+40).
Input: Jobs = [[1,2,100],[2,1,19],[3,2,27],[4,1,25],[5,1,15]]
Output: 2 127
Explanation: 2 jobs can be done with maximum profit of 127 (100+27).
Expected Time Complexity: O(nlogn)
Expected Auxilliary Space: O(n)

Constraints:
1 <= n <= 105
1 <= Deadline,id <= n
1 <= Profit <= 500
'''

def sequence(jobs,n):
    jobs.sort(key = lambda x : x.profit,reverse = True)
                                                                                            
    maxi = jobs[0].deadline 
    for i in range (1, n):
        maxi = max(maxi, jobs[i].deadline)
        
    slot = [-1] * (maxi +1)
    count = 0
    profit = 0
    
    
    for i in range (n):
        for j in range (jobs[i].deadline,0,-1):
            if slot[j] == -1 :
                slot[j] = i 
                count += 1  
                profit += jobs[i].profit   
                break
            
    return count, profit




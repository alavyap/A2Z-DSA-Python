'''

LeetCode :> https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1


Given arrival and departure times of all trains that reach a railway station. Find the minimum number of platforms required for the railway station so that no train is kept waiting.
Consider that all the trains arrive on the same day and leave on the same day. Arrival and departure time can never be the same for a train but we can have arrival time of one train equal to departure time of the other. At any given instance of time, same platform can not be used for both departure of a train and arrival of another train. In such cases, we need different platforms.

Note: Time intervals are in the 24-hour format(HHMM) , where the first two characters represent hour (between 00 to 23 ) and the last two characters represent minutes (this will be <= 59 and >= 0).

Examples:

Input: arr[] = [0900, 0940, 0950, 1100, 1500, 1800], 
            dep[] = [0910, 1200, 1120, 1130, 1900, 2000]
Output: 3
Explanation: There are three trains during the time 0940 to 1200. So we need minimum 3 platforms.
Input: arr[] = [0900, 1235, 1100], 
            dep[] = [1000, 1240, 1200]
Output: 1
Explanation: All train times are mutually exlusive. So we need only one platform
Input: arr[] = [1000, 0935, 1100], 
            dep[] = [1200, 1240, 1130]
Output: 3
Explanation: All 3 trains have to be their from 11:00 to 11:30
Expected Time Complexity: O(nLogn)
Expected Auxiliary Space: O(n)

Constraints:

1≤ number of trains ≤ 50000
0000 ≤ arr[i] ≤ dep[i] ≤ 2359


'''


def miniP(arr,dep):
    
    n = len(arr)
    arr.sort()
    dep.sort()
    
    neededP = 1 
    result = 1 
    i = 1 
    j = 0
    
    while  i < n and j < n :
        
        if arr[i] <= dep[j] :
            neededP += 1 
            i += 1 
            
        elif arr[i] > dep[j] :
            neededP -= 1 
            j += 1 
        
        result = max(result,neededP)
    return result
            
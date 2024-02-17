'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/merge-all-overlapping-intervals_6783452?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
LeetCode :>  https://leetcode.com/problems/merge-intervals/description/

Problem Statement: Given an array of intervals, merge all the overlapping intervals and return an array of non-overlapping intervals.
Example : 
Input: intervals=[[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] are overlapping we can merge them to form [1,6]
intervals.
'''

# Brute Force 
def mergeIntervals (arr):
    arr.sort()
    n = len(arr)
    ans = []
    for i in range (n):
        start = arr[i][0]
        end = arr[i][1]
        
        # Skipping the merged intervals 
        if ans and end <= ans[-1][1] :
            continue 
        
        # Checking the rest of the intervals 
        for j in range (i+1,n):
            
            # Checking 
            if arr[j][0] <= end :
                end = max(end,arr[j][1]) 
            else: 
                break 
        ans.append([start,end])         
           
    return ans

# Test Run 
# print(mergeIntervals([[1,3],[2,6],[8,10],[15,18]]))

# Optimal Approach 
def mergeOverlapping(arr):
    arr.sort() 
    n = len(arr)
    ans = []
    for i in range (n):
        if not ans  or arr[i][0] > ans[-1][1] :
            ans.append(arr[i])
            
        else :
            # If the current element lies in the last element of the interval 
            ans[-1][1] = max(ans[-1][1] , arr[i][1])
    return ans

    # arr.sort() 
    # n = len(arr)
    # ans = [] 
    # for i in range (n):
    #     if not ans or  arr[i][0] > ans[-1][1] :
    #         ans.append(arr[i])
    #     else :
    #         ans[-1][1] = max(arr[i][1],ans[-1][1])
    # return ans 
# Test Run 
print(mergeOverlapping([[1,3],[2,6],[8,10],[15,18]]))
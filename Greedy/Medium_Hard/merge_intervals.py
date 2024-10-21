'''
LeetCode :> https://leetcode.com/problems/merge-intervals/description/

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

'''



def merge(intervals):
    # Step 1: Sort intervals (think about which key to sort by)
    intervals.sort(key = lambda x : x[0])
    
    # Step 2: Initialize result list
    merged = []
    
    for interval in intervals:
        # If merged is empty or if current interval doesn't overlap with previous
        # Simply append current interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # There is an overlap, so we should merge
            # How should we merge?
            merged[-1][1] =max(merged[-1][1],interval[1])
                
    return merged
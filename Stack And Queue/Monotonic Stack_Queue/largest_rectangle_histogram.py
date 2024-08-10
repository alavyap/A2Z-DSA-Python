'''
LeetCode :> https://leetcode.com/problems/largest-rectangle-in-histogram/description/

 
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
'''
# Brute Force 
def largestR(heights):
    
    max_area = 0 
    n = len(heights)
    
    for i in range (n):
        min_height = float("inf")
        for j in range(i,n):
            min_height = min(min_height,heights[j])
            max_area = max(max_area, min_height* (j-i +1))
    return max_area



# Optimal Approach 

def rectangeH(heights):
    stack = []
    max_area = 0
    heights.append(0) #if the main stack becomes empty 
    
    for i,h in enumerate(heights): 
        start = i 
        
        while stack and stack[-1][1] > h :
            index,height = stack.pop() 
            max_area = max(max_area, height * (i -index))
            start = index 
        stack.append((start,h))
    return max_area    


a =  [2,1,5,6,2,3]
# a =  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print(largestR(a))
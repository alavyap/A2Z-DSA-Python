'''
Coding Ninja : > https://www.codingninjas.com/studio/problems/alternate-numbers_6783445?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
LeetCode :> https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

Rearrange Array Elements by Sign
Variety-1
Problem Statement:
There's an array 'A' of size 'N' with an equal number of positive and negative elements. 
Without altering the relative order of positive and negative elements, 
you must return an array of alternately positive and negative values.

Note: Start the array with positive elements.
Example:
Input:
arr[] = {1,2,-4,-5}, N = 4
Output:
1 -4 2 -5
Explanation: 
Positive elements = 1,2
Negative elements = -4,-5
To maintain relative ordering, 1 must occur before 2, and -4 must occur before -5.

'''

def reArrange (arr,n):
    count = 0 
    Pcount = 0 
    
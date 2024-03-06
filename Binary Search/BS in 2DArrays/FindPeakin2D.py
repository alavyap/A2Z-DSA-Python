'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/find-peak-element_7449073
LeetCode :> https://leetcode.com/problems/find-a-peak-element-ii/

Problem Statement : You are given a 0-indexed 2-D grid ‘g’ of size ‘n’ X ‘m’, where each cell contains a positive integer, and adjacent cells are distinct.
You need to find the location of a peak element in it. If there are multiple answers, find any of them.
A peak element is a cell with a value strictly greater than all its adjacent cells.
Assume the grid to be surrounded by a perimeter of ‘-1s’.
You must write an algorithm that works in O(n * log(m)) or O(m * log(n)) complexity.
Note:
In the output, you will see '0' or '1', where '0' means your answer is wrong, and '1' means your answer is correct.

Sample Input :
3 3
1 2 3
4 5 6
7 8 9   
Sample Output 2:
1
Explanation of sample output 2:
For g = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
Answer = [2,2].
There is only one peak element that is present at [2,2].
'''
# Brute Force > this was giving the output in the console but not in the other platform 
from turtle import right


def brute(arr):
    n = len(arr)
    m = len(arr[0])
    
    ans = float('-inf')
    
    for i in range (n):
        for j in range (m):
            # if arr[i][j] > ans :
            #     ans = arr[i][j] 
            ans = max(ans,arr[i][j])
            
    if ans :
        return [i,j]
    return [-1,-1]

# Test Run 
# print(brute([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


# Better Approach 
def better(arr):
    n = len(arr)
    m = len(arr[0])
    
    for i in range (n):
        for j in range (m):
            is_peak = True 
            
            if i > 0 :
                is_peak = is_peak and arr[i][j] > arr[i-1][j]
                
            if i < n -1 :
                is_peak = is_peak and arr[i][j] > arr[i+1][j]
                
            if j > 0 :
                is_peak = is_peak and arr[i][j] > arr[i][j-1]
                
            if j < m - 1 :
                is_peak = is_peak and arr[i][j] > arr[i][j+1]
            
            if is_peak :
                return 1 
    return 0


# Test Run 
# print(better([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


# Optimal Approach 
def optimal (arr):
    n = len(arr)
    m = len(arr[0])
    
    low = 0 
    high = m-1
    
    ans = [-1,-1]
    
    while (low <= high):
        mid = (low + high) // 2 
        
        row = maxiEl(arr,mid,n)
        
        left = arr[row][mid-1] if mid-1 >= 0 else -1
        right = arr[row][mid+1] if mid + 1 < m else -1
        
        if arr[row][mid] > left and arr[row][mid] > right :
            ans[0] = row 
            ans[1] = mid
            
            return ans 
        
        elif (arr[row][mid] < left):
            high = mid -1 
        else :
            low = mid + 1 
            
    return ans 

# Helper Function 
def maxiEl(arr,mid,n):
    max1 = float('-inf')
    ind = -1 
    
    for i in range (n):
        if arr[i][mid] > max1 :
            max1 = arr[i][mid]
            ind = i 
            
    return ind

# Test Run 
print(optimal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
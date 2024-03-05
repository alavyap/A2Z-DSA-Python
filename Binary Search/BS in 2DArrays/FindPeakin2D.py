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
# Brute Force 
def brute(arr):
    n = len(arr)
    m = len(arr[0])
    
    ans = float('-inf')
    
    for i in range (n):
        for j in range (m):
            if arr[i][j] > ans :
                ans = arr[i][j] 
        
            
            if ans :
                return "1"
    return "0"

# Test Run 
print(brute([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
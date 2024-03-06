'''
we will solve the most asked coding interview problem: Median of Row Wise Sorted Matrix
Problem Statement: Given a row-wise sorted matrix of size r*c, where r is no. of rows and c is no. of columns, find the median in the given matrix.
Assume - r*c is odd

Example 1:
Input: 
r = 3 , c = 3
1 4 9 
2 5 6
3 8 7
Output: Median = 5
Explanation: If we find the linear sorted array, the array becomes 1 2 3 4 5 6 7 8 9
So, median = 5
'''

# Brute Force 
def brute (arr):
    n = len(arr)
    m = len(arr[0])
    count = 0
    
    for i in range (n):
        for j in range (m):
            count += 1 
    
    ind = count // 2    
    return ind

# Test Run 
print(brute([     [ 1, 5, 7, 9, 11 ],
      [ 2, 3, 4, 8, 9 ],
      [ 4, 11, 14, 19, 20 ],
      [ 6, 10, 22, 99, 100 ],
      [ 7, 15, 17, 24, 28 ]   ]))
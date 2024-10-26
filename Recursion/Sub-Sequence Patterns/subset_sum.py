'''
GFG :> https://www.geeksforgeeks.org/problems/subset-sums2234/1


Given a list arr of n integers, return sums of all subsets in it. Output sums can be printed in any order.
 
Example :
Input:
n = 2
arr[] = {2, 3}
Output:
0 2 3 5
Explanation:
When no elements is taken then Sum = 0.
When only 2 is taken then Sum = 2.
When only 3 is taken then Sum = 3.
When element 2 and 3 are taken then 
Sum = 2+3 = 5.
Example 2:

Input:
n = 3
arr = {5, 2, 1}
Output:
0 1 2 3 5 6 7 8
Your Task:  
You don't need to read input or print anything. Your task is to complete the function subsetSums() which takes a list/vector and an integer n as an input parameter and returns the list/vector of all the subset sums.

Expected Time Complexity: O(2n)
Expected Auxiliary Space: O(2n)

Constraints:
1 <= n <= 15
0 <= arr[i] <= 104
'''

def subset_sum(arr,n):
    def backtrack(start,path):
        res.append(path[:])
        
        for i in range (start,n):
            path.append(arr[i])
            backtrack(i+1,path)
            path.pop()
            
    res = []
    backtrack(0,[])
    return [sum(inner) for inner in res]
            
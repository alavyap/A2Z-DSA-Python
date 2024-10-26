'''
Given an array of N integers and Q queries of indices. Return a list NGEs[] where NGEs[i] stores the count of elements strictly greater than the current element (arr[indices[i]]) to the right of indices[i].


Examples :

Input:  arr[]     = [3, 4, 2, 7, 5, 8, 10, 6]
        queries = 2
        indices[] = [0, 5]
Output:  6, 1
Explanation: The next greater elements to the right of 3(index 0) are 4,7,5,8,10,6. The next greater elements to the right of 8(index 5) is only 10.

Input:  arr[]     = [1, 2, 3, 4, 1]
        queries = 2
        indices[] = [0, 3]
Output:  3, 0
Explanation: The count of numbers to the right of index 0 which are greater than arr[0] is 3 i.e. (2, 3, 4). Similarly, the count of numbers to the right of index 3 which are greater than arr[3] is 0, since there are no greater elements than 4 to the right of the array.

Expected Time Complexity: O(N * queries).
Expected Auxiliary Space: O(queries).


Constraints:
1 <= N <= 104
1 <= arr[i] <= 105
1 <= queries <= 100

0 <= indices[i] <= N - 1


'''

# Brute Force 
def countNGE(arr,queries,indices):
    result=[]
    for i in indices:
        count=0
        for j in range(i+1,N):
            if arr[i]<arr[j]:
                count+=1
        result.append(count)
    return result




# Optimal Approach 
def ngeCount(N,arr,queries,indices):
    
    
    ans = []
    for i in range(queries):
        curr = arr[indices[i]]
        st = []
        r = N - 1
        while r > indices[i]:
            if arr[r] > curr:
                st.append(arr[r])
            r -= 1
        ans.append(len(st))
    return ans
        
   
        
   
  
     
        
arr = [3, 4, 2, 7, 5, 8, 10, 6]
N = len(arr)
queries = 2
indices = [0, 5]

# print(countNGE(arr,queries,indices))
print(ngeCount(N,arr,queries,indices))
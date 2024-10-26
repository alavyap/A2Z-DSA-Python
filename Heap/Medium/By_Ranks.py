'''
GFG :> https://www.geeksforgeeks.org/problems/replace-elements-by-its-rank-in-the-array/1

Given an array arr of N integers, the task is to replace each element of the array by its rank in the array. The rank of an element is defined as the distance between the element with the first element of the array when the array is arranged in ascending order. If two or more are same in the array then their rank is also the same as the rank of the first occurrence of the element. 

Example 1:

Input:
N = 6
arr = [20, 15, 26, 2, 98, 6]
Output:
4, 3, 5, 1, 6, 2
Explanation:
After sorting, array becomes {2,6,15,20,26,98}
Rank(2) = 1 (at index 0) 
Rank(6) = 2 (at index 1) 
Rank(15) = 3 (at index 2) 
Rank(20) = 4 (at index 3) and so on..
Example 2:

Input:
N = 4
arr = [2, 2, 1, 6]
Output:
2, 2, 1, 3
Explanation:
After sorting, array becomes {1, 2, 2, 6}
Rank(1) = 1 (at index 0) 
Rank(2) = 2 (at index 1) 
Rank(2) = 2 (at index 2) 
Rank(6) = 3 (at index 3)
Rank(6) = 3 because rank after 2 is 3 as rank 
of same element remains same and for next element 
increases by 1.
Your Task:
Complete the function int replaceWithRank(), which takes integer N  and an array of N integers as input and returns the list in which element at each position of original array is replaced by the rank of that element.

Expected Time Complexity: O(N * logN)
Expected Auxiliary Space: O(N)


Constraints:

1 <= N <= 105
1 <= arr[i] <= 109

'''

def arrange (N,arr):
    indexed_arr = list(enumerate(arr))
    
    indexed_arr.sort(key= lambda x:x[1])
    
    
    # Initialize rank and result array 
    rank = 1 
    result = [0] * N
    
    # Assign Ranks 
    for i in range (N):
        if i > 0 and indexed_arr[i][1] != indexed_arr[i-1][1]:
            rank += 1 
            
        result[indexed_arr[i][0]] = rank 
        
    return result

# Test 
N1 = 6
arr1 = [20, 15, 26, 2, 98, 6]
# print(arrange(N1,arr1)) 


# Without Built In Functions 

def replace_rank(arr,N) :
    if N == 0 :
        return []
    
    
    indexed_arr = [] 
    
    for i in range (N) :
        indexed_arr.append((i,arr[i]))
        
        
    quickSort(indexed_arr,0,N-1)
    
    
    rank = 1 
    result = [0] * N
    
    for i in range (N):
        
        if i > 0 and indexed_arr[i][1] != indexed_arr[i-1][1]:
            rank += 1
        result[indexed_arr[i][0]] = rank 
    return result



def quickSort(arr,low,high):
    
    if low < high :
        pi = partition(arr,low,high) 
        quickSort(arr,low,pi -1)
        quickSort(arr,pi+1, high)
        
        
def partition(arr,low,high):
    pivot = arr[high][1]
    
    i = low -1 
    for j in range (low,high):
        if arr[j][1] <= pivot :
            i += 1 
            arr[i],arr[j] = arr[j],arr[i]
    arr[i +1],arr[high] = arr[high],arr[i+1]
    return i+1



N= 6
arr = [20, 15, 26, 2, 98, 6]
print(replace_rank(arr,N)) 

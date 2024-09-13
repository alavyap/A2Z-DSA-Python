'''
GFG :> https://www.geeksforgeeks.org/problems/convert-min-heap-to-max-heap-1666385109/1

You are given an array arr of N integers representing a min Heap. The task is to convert it to max Heap.

A max-heap is a complete binary tree in which the value in each internal node is greater than or equal to the values in the children of that node. 

Example 1:

Input:
N = 4
arr = [1, 2, 3, 4]
Output:
[4, 2, 3, 1]
Explanation:

The given min Heap:

          1
        /   \
      2       3
     /
   4

Max Heap after conversion:

         4
       /   \
      2     3
    /
   1
Example 2:

Input:
N = 5
arr = [3, 4, 8, 11, 13]
Output:
[13, 11, 8, 3, 4]
Explanation:

The given min Heap:

          3
        /   \
      4      8
    /   \ 
  11     13

Max Heap after conversion:

          13
        /    \
      11      8
    /   \ 
   3     4
 

Your Task:
Complete the function int convertMinToMaxHeap(), which takes integer N and array represented minheap as input and converts it to the array representing maxheap. You don't need to return or print anything, modify the original array itself.

Note: Only an unique solution is possible under the expected time complexity.

Expected Time Complexity: O(N * log N)
Expected Auxiliary Space: O(N)


Constraints:

1 <= N <= 105
1 <= arr[i] <= 109  

'''

def maxi(arr):
    n = len(arr)
    
    for i in range ((n-2) // 2 ,-1, -1 ) :
        heapify(arr,n,i)
        
        
def heapify(arr,n,i) :
    largest = i 
    left = 2 * i + 1 
    right = 2 * i + 2 
    
    if left < n and arr[left] > arr[largest] :
        largest = left 
        
        
    if right < n and arr[right] > arr[largest] :
        largest = right
        

    if largest != i : 
        arr[i], arr[largest] = arr[largest], arr[i] 
        heapify(arr,n,largest)
        


arr = [1,2,3,4]
maxi(arr)
print (arr)
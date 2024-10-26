"""
Basic Operations of Heap [MIN and MAX]

GFG :> https://www.geeksforgeeks.org/problems/operations-on-binary-min-heap/1

A binary heap is a Binary Tree with the following properties:
1) Its a complete tree (All levels are completely filled except possibly the last level and the last level has all keys as left as possible). This property of Binary Heap makes them suitable to be stored in an array.

2) A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at the root must be minimum among all keys present in Binary Heap. The same property must be recursively true for all nodes in Binary Tree. Max Binary Heap is similar to MinHeap.

You are given an empty Binary Min Heap and some queries and your task is to implement the three methods insertKey,  deleteKey,  and extractMin on the Binary Min Heap and call them as per the query given below:
1) 1  x  (a query of this type means to insert an element in the min-heap with value x )
2) 2  x  (a query of this type means to remove an element at position x from the min-heap)
3) 3  (a query like this removes the min element from the min-heap and prints it ).

Example 1:

Input:
Q = 7
Queries:
insertKey(4)
insertKey(2)
extractMin()
insertKey(6)
deleteKey(0)
extractMin()
extractMin()
Output: 2 6 - 1
Explanation: In the first test case for
query 
insertKey(4) the heap will have  {4}  
insertKey(2) the heap will be {2 4}
extractMin() removes min element from 
             heap ie 2 and prints it
             now heap is {4} 
insertKey(6) inserts 6 to heap now heap
             is {4 6}
deleteKey(0) delete element at position 0
             of the heap,now heap is {6}
extractMin() remove min element from heap
             ie 6 and prints it  now the
             heap is empty
extractMin() since the heap is empty thus
             no min element exist so -1
             is printed.
Example 2:

Input:
Q = 5
Queries:
insertKey(8)
insertKey(9)
deleteKey(1)
extractMin()
extractMin()
Output: 8 -1
Your Task:
You are required to complete the 3 methods insertKey() which take one argument the value to be inserted, deleteKey() which takes one argument the position from where the element is to be deleted and extractMin() which returns the minimum element in the heap(-1 if the heap is empty)

Expected Time Complexity: O(Q*Log(size of Heap) ).
Expected Auxiliary Space: O(1).

Constraints:
1 <= Q <= 104
1 <= x <= 104

"""
curr_size = 0 
heap = [0 for i in range (101)]

def insertKey (x):
    global curr_size
    curr_size += 1 
    heap[curr_size] = x 
    shiftUp(curr_size) #type:ignore
    

# Helper Function 
def shiftUp(i):
    while i > 1 and heap[i] < heap[i // 2] : 
        heap[i], heap[i // 2] = heap[i //2 ], heap[i] 
        i = i // 2 

#Function to delete a key at ith index.
def deleteKey (i):
    global curr_size 
    i += 1
    if i < 1 or i > curr_size  :
        return 
    heap[i] = heap[curr_size]
    curr_size -= 1 
    if i <= curr_size :
        shiftDown(i)
        shiftUp(i) 
        
def shiftDown(i) :
    while 2 * i <= curr_size :
        j = 2 * i 
        if j < curr_size and heap[j] > heap[j + 1] :
            j += 1 
        if heap[i] <= heap[j] : 
            break 
        heap[i],heap[j] = heap[j],heap[i]
        i = j  
    

#Function to extract minimum value in heap and then to store 
#next minimum value at first index.
def extractMin ():
    global curr_size
    if curr_size < 1 :
        return -1 
    min_value = heap[1] 
    heap[1] = heap[curr_size]
    curr_size -= 1 
    shiftDown(1)
    return min_value





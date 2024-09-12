'''
Geeks for Geeks :> https://www.geeksforgeeks.org/problems/implementation-of-priority-queue-using-binary-heap/1


Given a binary heap implementation of Priority Queue. Extract the maximum element from the queue i.e. remove it from the Queue and return it's value. 

Examples :

Input: 4 2 8 16 24 2 6 5
Output: 24
Priority Queue after extracting maximum: 16 8 6 5 2 2 4
Input: 64 12 8 48 5
Output: 64
Priority Queue after extracting maximum: 48 12 8 5
Expected Time Complexity: O(logn)

Expected Space Complexity: O(n)

 

Constraints:

1<=n<=500


'''
#User function Template for python3

# 1. parent(i): Function to return the parent node of node i
# 2. leftChild(i): Function to return index of the left child of node i
# 3. rightChild(i): Function to return index of the right child of node i
# 4. shiftUp(int i): Function to shift up the node in order to maintain the
# heap property
# 5. shiftDown(int i): Function to shift down the node in order to maintain the
# heap property.
# int s=-1, current index value of the array H[].



# Brute force 
def extract(arr):
    n = len(arr)
    max = float("-inf")
    
    
    for ele in range (n):
        if max < arr[ele]:
            max = arr[ele]
            
    
    return max


# arr = [4,2,8,16,24,2,6,5]
arr = [64,12,8,48,5]

# print(extract(arr))


# GFG Code 
s = -1
H = [0] * 10009

def extract(self):
    global s 
    
    if s == -1 : 
        return None 
    
    
    max_val = H[0] #the root of the heap (maximum element) 
    H[0] = H[s] #Replace the root with the last element
    
    s -= 1 #Decrease the size of the heap 
    
    shiftDown(0)  # type: ignore #Restore the heap property strating from the root
    
    
    return max_val
    
    
# Importing Heap 

import heapq

def findK(arr,k):
    min_heap = [] 
    
    for num in arr :
        
        if len(min_heap) < k :
            heapq.heappush(min_heap,num)
            
            
        else :
            if num > min_heap[0] : 
                
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,num)
                
                
                
    return min_heap[0]
          

# arr = [1, 23, 12, 9, 30, 2, 50]
arr = [ 4,2,8,16,24,2,6,5]
k = 1
print(findK(arr,k))
'''
GFG :> https://www.geeksforgeeks.org/problems/implement-queue-using-array/1

Implement a Queue using an Array. Queries in the Queue are of the following type:
(i) 1 x   (a query of this type means  pushing 'x' into the queue)
(ii) 2     (a query of this type means to pop element from queue and print the poped element)

Examples:

Input:
Q = 5
Queries = 1 2 1 3 2 1 4 2
Output: 2 3
Explanation:
In the first test case for query 
1 2 the queue will be {2}
1 3 the queue will be {2 3}
2   poped element will be 2 the 
    queue will be {3}
1 4 the queue will be {3 4}
2   poped element will be 3 

Input:
Q = 4
Queries = 1 3 2 2 1 4   
Output: 3 -1
Explanation:
In the second testcase for query 
1 3 the queue will be {3}
2   poped element will be 3 the
    queue will be empty
2   there is no element in the
    queue and hence -1
1 4 the queue will be {4}. 
 

Expected Time Complexity: O(1) for both push() and pop().
Expected Auxiliary Space: O(1) for both push() and pop().

Constraints:
1 ≤ Q ≤ 105
0 ≤ x ≤ 105

'''

class Q :
    
    def __init__ (self):
        self.arr = [] 
        self.start = 0 
        self.rear = 0 
        
    def push(self, x):
         
         #add code here
        self.arr.append(x)
        self.rear += 1 
        
    #Function to pop an element from queue and return that element.
    def pop(self): 
         
        # add code here
        if self.start < self.rear:
            temp = self.arr[self.start]
            self.start += 1
            return temp
        return -1  # or raise an exception for empty queue
    
    
    
# Striver Code 

class Queue:
    def __init__(self):
        self.start = -1
        self.end = -1
        self.currSize = 0
        self.maxSize = 16
        self.arr = [0] * self.maxSize


    def push(self, newElement: int) -> None:
        if self.currSize == self.maxSize:
            print("Queue is full\nExiting...")
            exit(1)
        if self.end == -1:
            self.start = 0
            self.end = 0
        else:
            self.end = (self.end + 1) % self.maxSize
        self.arr[self.end] = newElement
        print("The element pushed is", newElement)
        self.currSize += 1


    def pop(self) -> int:
        if self.start == -1:
            print("Queue Empty\nExiting...")
        popped = self.arr[self.start]
        if self.currSize == 1:
            self.start = -1
            self.end = -1
        else:
            self.start = (self.start + 1) % self.maxSize
        self.currSize -= 1
        return popped


    def top(self) -> int:
        if self.start == -1:
            print("Queue is Empty")
            exit(1)
        return self.arr[self.start]


    def size(self) -> int:
        return self.currSize



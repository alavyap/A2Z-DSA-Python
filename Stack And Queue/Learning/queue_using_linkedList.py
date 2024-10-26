'''

GFG :> https://www.geeksforgeeks.org/problems/implement-queue-using-linked-list/1

Implement a Queue using Linked List. 
A Query Q is of 2 Types
(i) 1 x   (a query of this type means  pushing 'x' into the queue)
(ii) 2     (a query of this type means to pop an element from the queue and print the poped element)

Example 1:

Input:
Q = 5
Queries = 1 2 1 3 2 1 4 2
Output: 2 3
Explanation: n the first testcase
1 2 the queue will be {2}
1 3 the queue will be {2 3}
2   poped element will be 2 the
    queue will be {3}
1 4 the queue will be {3 4}
2   poped element will be 3.

Example 2:

Input:
Q = 4
Queries = 1 2 2 2 1 3 
Output: 2 -1
Explanation: In the second testcase 
1 2 the queue will be {2}
2   poped element will be {2} then
    the queue will be empty. 
2   the queue is empty and hence -1
1 3 the queue will be {3}.
Your Task:
Complete the function push() which takes an integer as input parameter and pop() which will remove and return an element(-1 if queue is empty).

Expected Time Complexity: O(1).
Expected Auxiliary Space: O(1).

Constraints:
1 <= Q <= 100
1 <= x <= 100


'''

class Node:
    
    def __init__(self,data):
        self.data = data 
        self.next = None 
        
        
class Queue:
    
    def __init__(self):
        self.start = None 
        self.rear = None 
        
        
    def push(self,item):
        
        newNode = Node(item)
        if self.empty():
            self.start = self.rear = newNode 
        else :
            self.rear.next = newNode 
            self.rear = newNode 
            

        
        
        
    
    def pop(self):
        if self.empty():
           return None 
        popped = self.start.data 
        self.start= self.start.next 
        if self.start is None :
            self.rear = None
        return popped 
    
        
        
        
    def peek(self):
        if self.empty():
            return None
        
        return self.start.data
        
        
    def empty(self):
      return self.stat is None
    
    def size(self):
        count = 0 
        current = self.start 
        while current :
            count += 1 
            current = current.next 
        return count
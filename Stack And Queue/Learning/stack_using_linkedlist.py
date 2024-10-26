'''
GFG :> https://www.geeksforgeeks.org/problems/implement-stack-using-linked-list/1

Let's give it a try! You have a linked list and must implement the functionalities push and pop of stack using this given linked list. Your task is to use the class as shown in the comments in the code editor and complete the functions push() and pop() to implement a stack. 
The push() method takes one argument, an integer 'x' to be pushed into the stack and pop() which returns an integer present at the top and popped out from the stack. If the stack is empty then return -1 from the pop() method.
Note: The input is given in the form of queries. Since there are two operations push() and pop(), there is two types of queries as described below:
(i) 1   (a query of this type takes x as another parameter and pushes it into the stack)
(ii) 2  (a query of this type means to pop an element from the stack and return the popped element)
Input is separated by space and as described above. 

Examples :

Input: [[1,2], [1,3], [2], [1,4], [2]]
Output: [3, 4]
Explanation: 
push(2)  : the stack will be {2}
push(3)  : the stack will be {2 3}
pop()    : poped element will be 3,the stack will be {2}
push(4)  : the stack will be {2 4}
pop()    : poped element will be 4
Input: [[2], [1,4], [1,5], [2]]
Output: [-1, 4]
Explanation: 
pop()    : the stack is empty so its -1.
push(4)  : the stack will be {4}
push(5)  : the stack will be {4 5}
pop()    : poped element will be 5, the stack will be {4}
Expected Time Complexity: O(1)
Expected Auxillary Space: O(1)

Constraints:
1 <= numbers of calls made to push, pop <= 100
1 <= x <= 100
'''

class LinkedList:
    def __init__ (self,data):
        self.data = data
        self.next = None 
        
        
        
class Stack :
    
    def __init__(self):
        self.top = None 
        
    def empty(self):
        return self.top is None 
    
    def push(self,data):
        
        newNode = LinkedList(data)
        newNode.next = self.top 
        self.top  = newNode
        
    def pop(self):
        if self.empty() :
            return -1 
        popped = self.top.data 
        self.top = self.top.next 
        return popped
    
    
    def peek(self):
        if self.empty() :
            return -1 
        return self.top.data
        
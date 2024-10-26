'''

LeetCode :> https://leetcode.com/problems/implement-queue-using-stacks/description/

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

Example 1:

s1
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
 

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.
 

Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.



'''
 
# Using two stacks 

from queue import LifoQueue
class MyQueue:

    
    def __init__(self):
        self.s1= LifoQueue()
        self.s2 = LifoQueue() 
    
    
    def push(self, x) :
        while not self.s1.empty() :
            self.s2.put(self.s1.get())
        self.s1.put(x)
        while not self.s2.empty() :
            self.s1.put(self.s2.get())
           
        
    def pop(self) :
        if self.s1.qsize() == 0 :
            exit(0)
        val = self.s1.get()
        return val 
    
    
    def peek(self) :
        if self.s1.qsize() == 0 :
            exit(0) 
        return self.s1.queue[-1]    

    def empty(self) :
        return self.s1.qsize() == 0

        
# Optimal Approach 


from queue import LifoQueue
class MyQueue:

    
    def __init__(self):
        self.s1= LifoQueue()
        self.s2 = LifoQueue() 
    
    
    def push(self, x) :
        self.s1.put(x)
        
    def pop(self) :
        if self.s2.empty() :
            while not self.s1.empty() :
                self.s2.put(self.s1.get())
        x = self.s2.get()
        return x 
    
    def peek(self) :
        if self.s2.empty() :
            while not self.s1.empty():
                self.s2.put(self.s1.get())
        return self.s2.queue[-1]

    def empty(self) :
        if  (self.s1.qsize() + self.s2.qsize()) == 0 :
            return True
        return False 

        



# Other way without using Inbuild libraries 
class MyQueue:

    def __init__(self):
        self.stack1 = []  # for push operations
        self.stack2 = []  # for pop and peek operations

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        self._transfer_if_needed()
        if self.stack2:
            return self.stack2.pop()
        return -1  # Or raise an exception if the queue is empty

    def peek(self) -> int:
        self._transfer_if_needed()
        if self.stack2:
            return self.stack2[-1]
        return -1  # Or raise an exception if the queue is empty

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def _transfer_if_needed(self) -> None:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

'''
LeetCode :> https://leetcode.com/problems/implement-stack-using-queues/description/


Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
 

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.
 

Follow-up: Can you implement the stack using only one queue?


'''
# Brute Force >>> Using Array 
class Ms:
    
    def __init__(self):
        self.maxS = 100
        self.arr = [0] * self.maxS 
        self.topE = -1

    def ph(self,x):
        if self.topE <  self.maxS -1 :
            self.topE += 1 
            self.arr[self.top] = x 
            
    def pp(self):
        if not self.empty():
            remove = self.arr[self.topE]
            self.topE -= 1
            return remove 
        return -1 
    
    def top(self):
        if not self.empty() :
            return self.arr[self.topE]
        return -1
    
    def empty(self):
        return self.topE == -1    
    
    
    
# Better  Approach >> using dobuble  queue


from collections import deque

class TStack :
    def __init__ (self):
        self.q1 = deque() 
        self.q2 = deque() 
        
        
    def push(self,x): 
        self.q2.append(x)
        while self.q1: 
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2,self.q1 

    
    def pop(self):
        
        if not  self.empty() :
            return self.q1.popleft()   # popleft() is a method specific to Python's deque (double-ended queue) data structure, which we're using to implement our queues in this stack simulation.
        return None 
    
    def top(self):
        if not self.empty() :
            return self.q1[0] 
        return None 
    
    def empty(self):
        return len(self.q1) == 0
    
    
# Optimal Approach >>> Using single queue

from queue import Queue
class OneQ :
    
    def __init__ (self):
        self.q = Queue()
        
        
    def push(self,x):
        s = self.q.qsize() 
        self.q.put(x)
        
        for i in range(s):
            self.q.put(self.q.get())
            
    
    def pop(self):
        if not self.q.empty():
            return self.q.get() 
        return None 
    
    def top(self):
        if not self.q.empty() :
            return self.q.queue[0] 
        return None
    def empty(self):
        return self.q.qsize() == 0
        
        
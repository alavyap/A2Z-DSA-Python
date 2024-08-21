'''
LeetCode :> https://leetcode.com/problems/lru-cache/description/

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
'''

# Optimal  Approach

class Node :
    def __init__(self,key,value):
        self.key = key 
        self.value = value 
        
        self.prev = None 
        self.next = None 
        
        
class LRUCache :
    def __init__(self, capacity):
        self.capacity = capacity 
        self.cache = {}  #key -> node
        
        
        # Create dummy head and tail nodes 
        self.head = Node (-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail 
        self.tail.prev = self.head 
        
        
    def _add_node(self,node):
        # Add the new node right after head 
        node.prev = self.head 
        node.next = self.head.next 
        
        
        self.head.next.prev = node 
        self.head.next = node 
        
        
        
    def _remove_node(self,node):
        
        # Remove an existing node from the linked list 
        prev_node = node.prev 
        next_node = node.next 
        
        prev_node.next = next_node
        next_node.prev  = prev_node 
        
        
    def _move_to_head(self,node):
        # Move certain node in between to the head 
        
        self._remove_node(node)
        self._add_node(node)
        
        
    def _pop_tail(self):
        # Pop the current tail 
        
        res = self.tail.prev 
        self._remove_node(res)
        return res
    
    
    def get(self,key):
        node = self.cache.get(key)
        if not node :
            return -1 
        
        
        # Move the accessed node to the head 
        self._move_to_head(node)
        return node.value 
    
    
    def put (self,key, value):
        node = self.cache.get(key)
        
        
        if not node :
            new_node = Node(key,value)
            self.cache[key] = new_node 
            self._add_node(new_node)
            
            
            if len(self.cache) > self.capacity :
                #  Pop the tail 
                tail = self._pop_tail() 
                del self.cache[tail.key]
        
        else : 
            # Update the value 
            node.value = value 
            self._move_to_head(node)
    
    

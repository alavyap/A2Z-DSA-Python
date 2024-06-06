'''
GFG :> https://www.geeksforgeeks.org/problems/flattening-a-linked-list/1
Coding Ninja :> https://www.naukri.com/code360/problems/flatten-a-linked-list_1112655
Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
(i) a next pointer to the next node,
(ii) a bottom pointer to a linked list where this node is head.
Each of the sub-linked-list is in sorted order.
Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. 

Note: The flattened list will be printed using the bottom pointer instead of the next pointer.
For more clarity have a look at the printList() function in the driver code.
Example :
Input:
5 -> 10 -> 19 -> 28
|     |     |     | 
7     20    22   35
|           |     | 
8          50    40
|                 | 
30               45
Output:  5-> 7-> 8- > 10 -> 19-> 20->
22-> 28-> 30-> 35-> 40-> 45-> 50.
Explanation:
The resultant linked lists has every 
node in a single level.
(Note: | represents the bottom pointer.)
'''

# Brute Force 
def flatten(head): 
    arr = [] 
    while head :
        temp = head 
        while temp :
            arr.append(temp.data)
            temp = temp.child
        head = head.next 
        
    arr.sort() 
    return arr   
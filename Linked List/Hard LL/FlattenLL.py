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
    tempo = head
    while tempo :
        temp = head 
        while temp :
            arr.append(temp.data)
            temp = temp.child
        tempo = tempo.next 
        
    # arr.sort() 
    return new_LL(arr)

def new_LL(arr):
    if not arr: 
        return None 
    
    head = Node(arr[0])
    tail = head
    
    for i in range (1,len(arr)):
        newNode = Node(arr[i])
        tail.child = newNode
        tail = newNode
        
    return head
# Time Complexity O(N*M) *2 + O(X logX) , where X = N*M & Space Complexity is O(N*M)*2



# Optimal Approach 


def flatLL(head):
    if head is None or head.next is None :
        return head 
    
    head_2 = flatLL(head.next)
    
    single_LL = merger(head,head_2)
    
    
    return single_LL

def merger(l1,l2):
    dummy = Node(-1)
    temp = dummy 
    
    while l1 and l2 :
        if l1.data < l2.data:
            temp.child = l1
            temp = l1
            l1 =l1.child 
        else :
            temp.child = l2 
            temp = l2 
            l2 = l2.child 
            
        temp.next = None 
        
        if l1 :
            temp.child = l1 
        else:
            temp.child = l2 
            
    if dummy.child :
        dummy.child.next = None 
        
    return dummy.child 

# Time : O(2*N*M) & Space : O(N) for recursive function 
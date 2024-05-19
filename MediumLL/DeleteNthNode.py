'''
LeetCode :> https://leetcode.com/problems/remove-nth-node-from-end-of-list/
CodingNinja :> https://www.naukri.com/code360/problems/delete-node-in-ll_5881?interviewProblemRedirection=true&search=Linked%20List

Problem Statement : Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example :
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

'''

# Brute Force 
def delNth(head,n):
    
    if head is None :
        return None 
    
    temp = head 
    count = 0 
    
    # Counting the length of the list 
    while (temp != None):
        count += 1 
        temp = temp.next 
        
    if count == n :
        newH = head.next 
        head = None 
        return newH 

    res = count - n 
    temp = head 
    while (temp != None) : 
        res -= 1
        if res == 0 :
            break 
        temp = temp.next 
        
    delN= temp.next 
    temp.next = temp.next.next 
    delN = None 
    return head


# Optimal Approch 

def deleN(head,n):
    
    
    hari = head 
    tori = head 
        
    for i in range (n):
        hari = hari.next
            
    while hari is None :
        # if not  hari  :
        return head.next
        
    while hari.next is not None  :
        tori = tori.next 
        hari = hari.next 
            
    tori.next = tori.next.next 
    return head


# Coding Ninja 
def deleteNth(head,pos):
    if head is None or pos <0 :
        return head 
    
    if pos == 0 :
        return head.next 
    
    temp = head 
    
    for i in range (pos -1):
        if temp.next is None :
            return head 
        temp = temp.next 
        
    if temp.next is None :
        return head 
    
    temp.next = temp.next.next 
    return head 
            
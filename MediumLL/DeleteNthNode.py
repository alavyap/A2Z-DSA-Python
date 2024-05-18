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
    
    # if head is None :
    #     return None 
    
    hari = head 
    tori = head 
    
    for i in range (n):
        hari = hari.next 
        
    while hari is None :
        return head.next
    
    while hari.next is not None :
        hari = hari.next 
        tori = tori.next 
        
    delNo = tori.next 
    tori.next = tori.next.next 
    delNo = None 
    return head
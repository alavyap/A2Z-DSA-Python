'''
Coding Ninja :> https://www.naukri.com/code360/problems/segregate-even-and-odd-nodes-in-a-linked-list_1116100?interviewProblemRedirection=true&search=Odd&attempt_status=COMPLETED&leftPanelTabValue=PROBLEM
LeetCode :> https://leetcode.com/problems/odd-even-linked-list/description/
Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example :
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

'''
# LeetCode Solution  

def oddEven(head):
    
    
    # if head is None or head.next is None :
    if not head : 
        return head 
    
    odd = head 
    even = head.next 
    headEven = even 
    
    while (even and odd and even.next and odd.next):
        odd.next = even.next 
        odd = odd.next 
        even.next = odd.next 
        even = even.next 
    odd.next = headEven 
    return head 


# Coding Ninja 
def EvenOdd(head):
    
    # We make 5 pointers 
    curr = head 
    even_head = None 
    even_tail = None 
    odd_head = None 
    odd_tail = None 
    
    while (curr != None):
        if curr.data%2 == 0 :
            if even_head is None :
                
                even_head = curr 
                even_tail = curr 
                
            else: 
                even_tail.next = curr 
                even_tail = curr 
                
        else: 
            if odd_head is None :
                odd_head = curr 
                odd_tail = curr 
            else: 
                odd_tail.next = curr 
                odd_tail = curr 
                
        curr = curr.next 
        
    if even_head and odd_head :
        even_tail.next = odd_head 
        odd_tail.next = None 
        
    return even_head if even_head else odd_head
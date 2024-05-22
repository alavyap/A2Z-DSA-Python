'''

LeetCode :> https://leetcode.com/problems/sort-list/description/
Coding Ninja :> https://www.naukri.com/code360/problems/sort-linked-list_920517?interviewProblemRedirection=true&search=sort%20link
Problem Statement: Given the head of a linked list, return the list after sorting it in ascending order.
Example :
Input: head = [4,2,1,3]
Output: [1,2,3,4]

🚨🚨🚨🚨🚨🚨 Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)? 🚨🚨🚨🚨🚨🚨🚨
'''

# Brute Force / NeetCode  
# Time and Space Complexity is O(NlogN) and O(N)

class ListNode:
    def __init__ (self,val):
        self.val = val


def sortLi(self,head):
    
    # Edge Case 
    if head is None or head.next is None :
        return head 
    
    left = head 
    right = self.getMid(head)
    temp = right.next 
    right.next = None 
    right = temp 
    
    
    left = self.sortLi(left)
    right = self.sortLi(right)
    
    return self.merge(left,right)


def getMid(self,head):
    if head is None or head.next is None : 
        return head 
    
    slow = head 
    fast = head 
    
    while fast.next is not None and fast.next.next is not None :
        slow = slow.next 
        fast = fast.next.next 
    return slow


def merge(self,left,right):
    tail = dummy = ListNode() 
    
    while left and right :
        if left.val < right.val :
            tail.next = left
            left = left.next 
        else :
            tail.next = right 
            right = right.next 
        tail = tail.next
        
        if left :
            tail.next = left 
        if right :
            tail.next = right
    return dummy.next


# Code with Space Complexity of O(1)

def sortList(head):
 
    dummy = ListNode(0)
    dummy.next = head  
    
    
    # Grab sublists of size 1,then 2, then 4 etc until fully merged 
    steps = 1
    while True :
        
        # Record the progress of the current pass intor a single semi sorted list by updating
        # the next of the previous node (or the dummy on the first loop)
        prev = dummy 
        
        
        # Keep track of how much is left to process on this pass of the lists
        remaining = prev.next 
        
        # while the current pass though the list has not been completed
        num_loops = 0 
        while remaining :
            num_loops += 1
            
            # Split 2 sublists of steps length from the front 
            sublists = [None,None]
            sublists_tail = [None,None]
            
            
            for i in range (2):
                sublists[i] = remaining
                substeps = steps 
                
                while substeps and remaining :
                    substeps -= 1 
                    sublists_tail[i] = remaining
                    remaining = remaining.next 
                # Ensure the sublists (if one was made) is terminated 
                if sublists_tail[i] :
                    sublists_tail[i].next = None 
                    
            
            # We have two sublists of (upto) length step that are sorted, merged them onto
            # the end into a single list of (upto) steps * 2 
            
            while sublists[0] and sublists[1] :
                if sublists[0].val <= sublists[1].val :
                    prev.next = sublists[0] 
                    sublists[0] = sublists[0].next 
                else:
                    prev.next = sublists[1] 
                    sublists[1] = sublists[1].next 
                prev = prev.next
               
            
            # One list has been finished, attach what ever is left of the other to the end 
            if sublists[0] :
                prev.next = sublists[0] 
                prev = sublists_tail[0] 
            else:
                prev.next  = sublists[1]
                prev = sublists_tail[1] 
        
        # Double the steps each go around 
        
        steps *= 2 
        
        # If the entire lsist was fully processed in a single loop, it means we've completely sorted the list and are done 
        
        if 1 >= num_loops :
            return dummy.next
                
            
            
    
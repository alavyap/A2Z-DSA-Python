'''
GFG :> https://www.geeksforgeeks.org/problems/sort-a-stack/1

Given a stack, the task is to sort it such that the top of the stack has the greatest element.

Example :
Input:
Stack: 3 2 1
Output: 3 2 1

Your Task: 
You don't have to read input or print anything. Your task is to complete the function sort() which sorts the elements present in the given stack. (The sorted stack is printed by the driver's code by popping the elements of the stack.)

Expected Time Complexity: O(N*N)
Expected Auxilliary Space: O(N) recursive.
'''

# Brute force 
def ssort(s):
    res = s.sort()
    return res 

# Optimal Approach 
def sort(s):
    """
    The function sorts a stack in ascending order using recursion.
    
    :param s: The `s` parameter in the `sort` function is a stack that contains elements to be sorted in
    non-decreasing order. The `stack_insert` function is used to insert an element into a stack while
    maintaining the order. The code recursively sorts the stack `s` by popping elements and inserting
    :return: The `sort` function is a recursive function that sorts a stack in ascending order. The
    `stack_insert` function is a helper function used by the `sort` function to insert an element in the
    correct position in the stack. The `sort` function sorts the stack by recursively popping elements
    from the stack and inserting them in the correct position using the `stack_insert` function. The
    sorted stack is
    """
    if not s :
        return 
    top = s.pop() 
    
    sort(s)
    stack_insert(s,top)
    
    
def stack_insert(stack,element):
    if not stack or stack[-1] <= element :
        stack.append(element)
        return 
    top = stack.pop() 
    
    stack_insert(stack,element)
    
    stack.append(top)
    
    
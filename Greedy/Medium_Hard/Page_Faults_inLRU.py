'''
GFG :> https://www.geeksforgeeks.org/problems/page-faults-in-lru5603/1

In operating systems that use paging for memory management, page replacement algorithm is needed to decide which page needs to be replaced when the new page comes in. Whenever a new page is referred and is not present in memory, the page fault occurs and Operating System replaces one of the existing pages with a newly needed page.

Given a sequence of pages in an array pages[] of length N and memory capacity C, find the number of page faults using Least Recently Used (LRU) Algorithm. 

Note:- Before solving this example revising the OS LRU cache mechanism is recommended.

Example 1:

Input: N = 9, C = 4
pages = {5, 0, 1, 3, 2, 4, 1, 0, 5}
Output: 8
Explaination: memory allocated with 4 pages 5, 0, 1, 
3: page fault = 4
page number 2 is required, replaces LRU 5: 
page fault = 4+1 = 5
page number 4 is required, replaces LRU 0: 
page fault = 5 + 1 = 6
page number 1 is required which is already present: 
page fault = 6 + 0 = 6
page number 0 is required which replaces LRU 3: 
page fault = 6 + 1 = 7
page number 5 is required which replaces LRU 2: 
page fault = 7 + 1  = 8.
Your Task:
You do not need to read input or print anything. Your task is to complete the function pageFaults() which takes N, C and pages[] as input parameters and returns the number of page faults.

Expected Time Complexity: O(N*C)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 1000
1 ≤ C ≤ 100
1 ≤ pages[i] ≤ 1000


'''
def faults(N,C,pages):
    
    memory = [] 
    page_faults = 0 
    
    for page in pages :
        
        if page not in memory :
            page_faults += 1 
            
            if len(memory) < C :
                memory.append(page)
            else :
                memory.pop(0)
                memory.append(page)
        else :
            memory.remove(page)
            memory.append(page)
    return page_faults


N=9
C = 4
pages = [5, 0, 1, 3, 2, 4, 1, 0, 5]


print(faults(N,C,pages))
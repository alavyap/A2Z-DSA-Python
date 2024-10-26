'''
Let’s say we have to print integers starting from 0 till 2 only, this will be how the pseudocode for it will look like
'''

# Striver Code in Python
cnt = 0

def print_count():
    global cnt

    # Base Condition
    if cnt == 3:
        return

    print(cnt)
    
    # Count Incremented
    cnt += 1
    print_count()

# my approach
def count ():
    i = 0 
    while (i <3):
        print(i)
        i +=1

count()
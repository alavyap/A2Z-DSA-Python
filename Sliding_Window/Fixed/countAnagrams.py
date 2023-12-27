'''

Given a word pat and a text txt. Return the count of the occurences of anagrams of the word in the text.

Example 1:
Input:
txt = forxxorfxdofr
pat = for
Output: 3
Explanation: for, orf and ofr appears
in the txt, hence answer is 3.

Example 2:
Input:
txt = aabaabaa
pat = aaba
Output: 4
Explanation: aaba is present 4 times
in txt. . 

'''

def countAnagram(txt,pat):
    
    # this code is getting the length of the txt and pat array
    txt_len, pat_len = len(txt), len(pat)
    
    # this is a empty dictionary that will store the words as key and there count as value which are inside the pat array
    pat_count = {}
    for char in pat:
        pat_count[char] = pat_count.get(char, 0) + 1
        
    # this will count the occurrences of characters inside the window {initial window}
    window_count =  {}
    for char in txt[:pat_len]:
        window_count[char] = window_count.get(char,0) + 1
        
    # this is the main count variable which will check if the characters in pat_count and window_count are same or not 
    count = 0
    
    # this will check if they are equal or not, if equal the count will be increased by 1 
    if pat_count == window_count :
        count += 1
        
    # this will slide the window after the window is checked with pat
    for i in range (pat_len, txt_len):
        
        # this will add one character to the window 
        window_count[txt[i]] = window_count.get(txt[i], 0) + 1 
        
        # this will remove the leftcharacter from the window when the window is move by 1 
        if window_count[txt[i - pat_len]] == 1 :
            del window_count[txt[i - pat_len]]
     
        # if that condition is not true the 
        else: 
            window_count[txt[i - pat_len]] -= 1
            
            
        # check if the current window character is same as pat_count {anagram} or not  >> then increase count by 1 
        if pat_count == window_count :
            count+=1
            
    return count
            
    

print(countAnagram("forxxorfxdofr","for"))
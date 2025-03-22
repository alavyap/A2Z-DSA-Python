'''
Link :> https://leetcode.com/problems/word-ladder-ii/description/


A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 5
endWord.length == beginWord.length
1 <= wordList.length <= 500
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
The sum of all shortest transformation sequences does not exceed 105.
'''


from collections import defaultdict, deque
from unittest import result


def wordLadder2(beginWord,endWord,wordList):
    
    wordSet = set(wordList)
    queue = set() 
    result = [] 
    queue.add(beginWord)
    parent = defaultdict(set)
    
    while queue :
        new_queue = set() 
        for currentWord in queue:
            for i in range (len(beginWord)) :
                for c in "abcdefghijklmnopqrstuvwxyz" :
                    newWord = currentWord[:i] +c + currentWord[i+1:]
                    
                    if newWord in wordSet and newWord != currentWord :
                        parent[newWord].add(currentWord)
                        new_queue.add(newWord)
                        
        wordSet -= new_queue
        queue = new_queue
        
        
    def build_path(last,lst):
        if last == beginWord :
            result.append(list(reversed(lst)))
            return 
        for word in parent[last]:
            build_path(word, lst + [word])
    build_path(endWord,[endWord])
    return result
        
            
    
    
    
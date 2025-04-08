'''
Link :> https://www.lintcode.com/problem/892/ ||   https://leetcode.com/problems/alien-dictionary/editorial/


There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

You may assume all letters are in lowercase
At first different letter, if the letter in s precedes the letter in t in the given list order, then the dictionary order of s is less than t
The dictionary is invalid, if string a is prefix of string b and b is appear before a
If the order is invalid, return an empty string
There may be multiple valid order of letters, return the smallest in normal lexicographical order
The letters in one string are of the same rank by default and are sorted in Human dictionary order
Example
Example 1:

Input：["wrt","wrf","er","ett","rftt"]
Output："wertf"
Explanation：
from "wrt"and"wrf" ,we can get 't'<'f'
from "wrt"and"er" ,we can get 'w'<'e'
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rftt" ,we can get 'e'<'r'
So return "wertf"
Example 2:

Input：["z","x"]
Output："zx"
Explanation：
from "z" and "x"，we can get 'z' < 'x'
So return "zx"
'''

from collections import defaultdict, deque

def alienOrder(words):
    # Step 1: Initialize graph and in-degree map
    graph = defaultdict(set)
    in_degree = {char: 0 for word in words for char in word}

    # Step 2: Build graph
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i+1]
        min_len = min(len(word1), len(word2))
        
        # Edge case: prefix issue
        if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
            return ""
        
        for j in range(min_len):
            if word1[j] != word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                break

    # Step 3: Topological sort using BFS
    queue = deque([char for char in in_degree if in_degree[char] == 0])
    order = []

    while queue:
        char = queue.popleft()
        order.append(char)
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Check if valid topological sort
    return ''.join(order) if len(order) == len(in_degree) else ""

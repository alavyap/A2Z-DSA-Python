'''
Link :> https://www.naukri.com/code360/problems/implement-trie_1387095


Problem statement
Ninja has to implement a data structure ”TRIE” from scratch. Ninja has to complete some functions.

1) Trie(): Ninja has to initialize the object of this “TRIE” data structure.

2) insert(“WORD”): Ninja has to insert the string “WORD”  into this “TRIE” data structure.

3) countWordsEqualTo(“WORD”): Ninja has to return how many times this “WORD” is present in this “TRIE”.

4) countWordsStartingWith(“PREFIX”): Ninjas have to return how many words are there in this “TRIE” that have the string “PREFIX” as a prefix.

5) erase(“WORD”): Ninja has to delete one occurrence of the string “WORD” from the “TRIE”.
Note:

1. If erase(“WORD”) function is called then it is guaranteed that the “WORD” is present in the “TRIE”.

2. If you are going to use variables with dynamic memory allocation then you need to release the memory associated with them at the end of your solution.
Can you help Ninja implement the "TRIE" data structure?

Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= “T” <= 50
1 <= “N” <= 10000
 “WORD” = {a to z}
1 <= | “WORD” | <= 1000

Where “T” is the number of test cases, “N” denotes how many times the functions(as discussed above) we call, “WORD” denotes the string on which we have to perform all the operations as we discussed above, and | “WORD” | denotes the length of the string “WORD”.

Time limit: 1 sec.
Sample Input 1:
1
5
insert coding
insert ninja
countWordsEqualTo coding
countWordsStartingWith nin
erase coding
Sample Output 1:
1
1   
Explanation of sample input 1:
After insertion of “coding” in “TRIE”:

After insertion of “ninja” in “TRIE”:

Count words equal to “coding” :

Count words those prefix is “nin”:

After deletion of the word “coding”, “TRIE” is:

Sample Input 2:
1
6
insert samsung
insert samsung
insert vivo
erase vivo
countWordsEqualTo samsung
countWordsStartingWith vi
Sample Output 2:
2
0
Explanation for sample input 2:
insert “samsung”: we are going to insert the word “samsung” into the “TRIE”.

insert “samsung”: we are going to insert another “samsung” word into the “TRIE”.

insert “vivo”: we are going to insert the word “vivo” into the “TRIE”.

erase “vivo”: we are going to delete the word “vivo” from the “TRIE”.

countWordsEqualTo “samsung”: There are two instances of “sumsung” is present in “TRIE”.

countWordsStartingWith “vi”: There is not a single word in the “TRIE” that starts from the prefix “vi”.
'''


class Node :
    
    def __init__(self):
        self.links = [None] * 26
        self.cntEndWith = 0 
        self.cntPrefix = 0 
        
    def contains_key(self,ch):
        return self.links[ord(ch) - ord("a")] is not None
    
    def get(self,ch):
        return self.links[ord(ch) - ord("a")]    
    
    def put(self,ch,node):
        self.links[ord(ch) - ord("a")] = node 
        
    def increase_end(self):
        self.cntEndWith += 1
        
    def increase_prefix(self):
        self.cntPrefix +=1
        
    def delete_end(self):
        self.cntEndWith -= 1 
        
    def reduce_prefix(self):
        self.cntPrefix -= 1 
    
    
    


class Trie:
    def __init__(self):
        # Write your code here.
        self.root = Node()

    def insert(self, word):
        # Write your code here.
        node = self.root
        for ch in word:
            if not node.contains_key(ch):
                node.put(ch,Node())
            node = node.get(ch)
            node.increase_prefix()
        node.increase_end()
        
        
        
    def countWordsEqualTo(self, word):
        node = self.root
        
        for ch in word: 
            if node.contains_key(ch):
                node = node.get(ch)
            else:
                return 0 
        return node.cntEndWith

    def countWordsStartingWith(self, word):
        node = self.root
        
        for ch in word: 
            if node.contains_key(ch):
                node = node.get(ch)
            else:
                return 0
        return node.cntPrefix

    def erase(self, word):
        # Write your code here.
        node = self.root
        
        for ch in word:
            if node.contains_key(ch):
                node = node.get(ch)
                node.reduce_prefix()
            else:
                return 
        node.delete_end()

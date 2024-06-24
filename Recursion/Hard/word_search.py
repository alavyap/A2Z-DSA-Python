'''

LeetCode :> https://leetcode.com/problems/word-search/description/


Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
'''

# Time Complexity :. O(4 (N∗M))

def exist(self,board, word):
    row = len(board)
    col = len(board[0])


    # find the first letter in board of word 
    for r in range (row):
        for c in range (col):
            if board[r][c] == word[0] :
                if self.searchNext(board, word, 0, r, c, row, col):
                    return True 
    return False


def searchNext(self,board, word, index, r, c, row, col):
        
    #  if the index reaches the end that means we have found the word
    if index == len(word):
        return True
    
    # checking the boundaries if the character at which we are placed is not the required letter
    if r < 0 or c < 0 or r >= row or c >= col or board[r][c] != word[index] or board[r][c] == '!':
        return False
    
    # this is to prevent the reusing of the same character
    current_letter = board[r][c] 
    board[r][c] = '!'
    
    # Finding the next letter in all 4 directions in the matrix
    # top of the current position
    top = self.searchNext(board, word, index + 1, r - 1, c, row, col)
    
    # bottom of the current position
    bottom = self.searchNext(board, word, index + 1, r + 1, c, row, col)

    # right of the current position
    right = self.searchNext(board, word, index + 1, r, c + 1, row, col)

    # left of the current position
    left = self.searchNext(board, word, index + 1, r, c - 1, row, col)
    
    board[r][c] = current_letter  #reverting the changes 
    
    return top or bottom or left or right


# 
# Follow up: Could you use search pruning to make your solution faster with a larger board?
def existing(self, board, word) -> bool:
    row = len(board)
    col = len(board[0])
        
        # Frequency check
    board_counter = Counter(char for row in board for char in row)
    word_counter = Counter(word)
        
    for char in word_counter:
        if word_counter[char] > board_counter[char]:
            return False
        
    def backtrack(i, j, k):
        if k == len(word):
            return True
        if i < 0 or i >= row or j < 0 or j >= col or board[i][j] != word[k]:
            return False
            
        temp = board[i][j]
        board[i][j] = ''
            
        found = (backtrack(i+1, j, k+1) or
                backtrack(i-1, j, k+1) or
                backtrack(i, j+1, k+1) or
                backtrack(i, j-1, k+1))
            
        board[i][j] = temp
        return found
        
    for r in range(row):
        for c in range(col):
            if board[r][c] == word[0]:
                if backtrack(r, c, 0):
                    return True
    return False
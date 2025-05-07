'''
Link :> https://www.lintcode.com/problem/434/  || https://leetcode.com/problems/number-of-islands-ii/description/

Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k). Originally, the 2D matrix is all 0 which means there is only sea in the matrix. The list pair has k operator and each operator has two integer A[i].x, A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island. Return how many island are there in the matrix after each operator.You need to return an array of size K.

0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Example
Example 1:

Input: n = 4, m = 5, A = [[1,1],[0,1],[3,3],[3,4]]
Output: [1,1,2,2]
Explanation:
0.  00000
    00000
    00000
    00000
1.  00000
    01000
    00000
    00000
2.  01000
    01000
    00000
    00000
3.  01000
    01000
    00000
    00010
4.  01000
    01000
    00000
    00011
Example 2:

Input: n = 3, m = 3, A = [[0,0],[0,1],[2,2],[2,1]]
Output: [1,1,2,2]



'''
class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False  # already in same set
        # Union by rank
        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        elif self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        else:
            self.parent[yr] = xr
            self.rank[xr] += 1
        return True
    
    
def main(n,m,positions):
    dsu = DSU(n * m)
    grid = [[0] * m for _ in range(n)]
    result = []
    count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    land = set()

    for x, y in positions:
        if (x, y) in land:
            result.append(count)
            continue

        land.add((x, y))
        grid[x][y] = 1
        count += 1
        index = x * m + y

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            nindex = nx * m + ny
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                if dsu.union(index, nindex):
                    count -= 1

        result.append(count)

    return result
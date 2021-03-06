"""
994. Rotting Oranges
Medium

1200

169

Add to List

Share
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.

"""
import collections

class Solution(object):
    def rottenOranges(self, grid):
        row, col = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        fresh_oranges = set()
        rotten = collections.deque()
        minutes=0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh_oranges.add((i, j))
                elif grid[i][j] == 2:
                    rotten.append([i, j, minutes])
        while rotten:
            x, y , minutes = rotten.popleft()
            for dx, dy in directions:
                if 0<=x+dx<row and 0<=y+dy<col and grid[x+dx][y+dy] == 1:
                    grid[x+dx][y+dy] = 2
                    fresh_oranges.remove((x+dx, y+dy))
                    rotten.append([x+dx, y+dy, minutes+1])
        return minutes if not fresh_oranges else -1
                

print(Solution().rottenOranges(
[[2,1,1],[1,1,0],[0,1,1]]))
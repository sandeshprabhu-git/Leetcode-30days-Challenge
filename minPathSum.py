"""
Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

"""

class Solution:
    def minPathSum(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    if j == 0:
                        dp[i][j] = grid[i][j]
                    else:
                        dp[i][j] = dp[i][j-1] + grid[i][j]
                else:
                    if j == 0:
                        dp[i][j] = dp[i-1][j] + grid[i][j]
                    else:
                        dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])
        return dp[-1][-1]



print(Solution().minPathSum([
    [1,3,1],
    [1,5,1],
    [4,2,1]
]))
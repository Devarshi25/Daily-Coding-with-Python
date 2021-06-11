class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        num_paths = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    num_paths[i][j] = 0
                else:
                    if i == 0:
                        if j == 0:
                            num_paths[i][j] = 1 - obstacleGrid[i][j]
                        else:
                            num_paths[i][j] = num_paths[i][j-1]
                    elif j == 0:
                        num_paths[i][j] = num_paths[i-1][j]
                    else:
                        num_paths[i][j] = num_paths[i][j-1] + num_paths[i-1][j]

        return num_paths[i][j]


obstacleGrid = [[0, 0, 1], [0, 0, 1], [1, 0, 0]]
print(Solution().uniquePathsWithObstacles(obstacleGrid))

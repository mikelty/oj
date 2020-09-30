import unittest


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0]*n for _ in range(m)]
        s=False
        for i in range(m):
            if obstacleGrid[i][0]==1:
                s=True
            if not s:
                dp[i][0]=1
        s=False
        for i in range(n):
            if obstacleGrid[0][i]==1:
                s=True
            if not s:
                dp[0][i]=1
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i-1][j]==0:
                    dp[i][j]+=dp[i-1][j]
                if obstacleGrid[i][j-1]==0:
                    dp[i][j]+=dp[i][j-1]
        if obstacleGrid[m-1][n-1]==1:
            return 0
        return dp[m-1][n-1]


class MyTest(unittest.TestCase):
    def test_1(self):
        obstac=[
                  [0,0,0],
                  [0,1,0],
                  [0,0,0]
                ]
        ans=2
        self.assertEqual(Solution().uniquePathsWithObstacles(obstac),ans)



if __name__=='__main__':
    unittest.main()
import unittest


class Solution:
    def minPathSum(self, grid) -> int:
        r,c=len(grid),len(grid[0])
        for i in range(r):
            for j in range(c):
                a,b=-1,-1
                if i>0:
                    a=grid[i-1][j]
                if j>0:
                    b=grid[i][j-1]
                if a!=-1 and b!=-1:
                    grid[i][j]+=min(a,b)
                elif a!=-1:
                    grid[i][j]+=a
                elif b!=-1:
                    grid[i][j]+=b
        #print(grid)
        return grid[r-1][c-1]


class MyTest(unittest.TestCase):
    def test_1(self):
        grid=[
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]
        ans=7
        self.assertEqual(Solution().minPathSum(grid),ans)


if __name__=='__main__':
    unittest.main()
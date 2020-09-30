#note this solution is faster than any dp solutions when m and n gets large


import unittest


class Solution:
    def factorial(self, k):
        if k < 0:
            return 0
        if k < 2:
            return 1
        return k * self.factorial(k - 1)

    def choose(self, n, k):
        if n < k:
            return 0
        if n == k:
            return 1
        o = 1
        for i in range(n - k + 1, n + 1):
            o *= i
        return o // self.factorial(k)

    def uniquePaths(self, m: int, n: int) -> int:
        # stars&bars
        return self.choose(n + m - 2, n - 1)


class MyTest(unittest.TestCase):
    def test_1(self):
        m=3
        n=7
        ans=28
        self.assertEqual(Solution().uniquePaths(m,n),ans)

    def test_2(self):
        m=3
        n=2
        ans=3
        self.assertEqual(Solution().uniquePaths(m,n),ans)

    def test_3(self):
        m=7
        n=3
        ans=28
        self.assertEqual(Solution().uniquePaths(m,n),ans)

    def test_4(self):
        m=3
        n=3
        ans=6
        self.assertEqual(Solution().uniquePaths(m,n),ans)


if __name__=='__main__':
    unittest.main()
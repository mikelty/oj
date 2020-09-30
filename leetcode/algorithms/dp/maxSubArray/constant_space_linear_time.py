import unittest


class Solution:
    def maxSubArray(self, n) -> int:
        if not n:
            return 0
        c=m=n[0]
        for e in n[1:]:
            c=max(e,c+e)
            m=max(m,c)
        return m


class MyTest(unittest.TestCase):
    def test_1(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        ans=6
        self.assertEqual(Solution().maxSubArray(nums),ans)

    def test_2(self):
        nums = [1]
        ans=1
        self.assertEqual(Solution().maxSubArray(nums),ans)

    def test_1(self):
        nums = [0]
        ans=0
        self.assertEqual(Solution().maxSubArray(nums),ans)

    def test_1(self):
        nums = [-1]
        ans=-1
        self.assertEqual(Solution().maxSubArray(nums),ans)

    def test_1(self):
        nums = [-2147483647]
        ans = -2147483647
        self.assertEqual(Solution().maxSubArray(nums), ans)


if __name__=='__main__':
    unittest.main()
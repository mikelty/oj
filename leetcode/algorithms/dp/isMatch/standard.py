#this is regex matching
#idea from https://leetcode.com/problems/regular-expression-matching/discuss/5723/My-DP-approach-in-Python-with-comments-and-unittest


import unittest
from collections import defaultdict


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp=[[False]*(len(s)+1) for _ in range(len(p)+1)]
        dp[0][0]=True
        for i in range(2,len(p)+1):
            dp[i][0]=dp[i-2][0] and p[i-1]=='*'
        for i in range(1,len(p)+1):
            for j in range(1,len(s)+1):
                if p[i-1]!='*':
                    dp[i][j]=dp[i-1][j-1] and \
                             (p[i-1]==s[j-1] or p[i-1]=='.')
                else:
                    dp[i][j]=dp[i-2][j] or dp[i-1][j]
                    if p[i-2]==s[j-1] or p[i-2]=='.':
                        dp[i][j]|=dp[i][j-1]
        return dp[-1][-1]


class MyTest(unittest.TestCase):
    def test_1(self):
        s = "aa"
        p = "a"
        self.assertFalse(Solution().isMatch(s, p))

    def test_2(self):
        s = "ab"
        p = ".*"
        self.assertTrue(Solution().isMatch(s, p))


    def test_3(self):
        s = "aab"
        p = "c*a*b"
        self.assertTrue(Solution().isMatch(s, p))


    def test_4(self):
        s = "mississippi"
        p = "mis*is*p*."
        self.assertFalse(Solution().isMatch(s, p))


if __name__=='__main__':
    unittest.main()
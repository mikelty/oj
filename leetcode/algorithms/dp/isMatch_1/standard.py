import unittest


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        S,P=len(s),len(p)
        dp=[[False]*(P+1) for _ in range(S+1)]
        dp[S][P]=True
        for j in reversed(range(P)):
            if p[j]!='*':
                break
            dp[S][j]=True
        for i in reversed(range(S)):
            for j in reversed(range(P)):
                if s[i]==p[j] or p[j]=='?':
                    dp[i][j]=dp[i+1][j+1]
                elif p[j]=='*':
                    dp[i][j]=dp[i+1][j] or dp[i][j+1]
                else:
                    dp[i][j]=False
        return dp[0][0]


class MyTest(unittest.TestCase):
    def test_1(self):
        s = "aa"
        p = "a"
        self.assertFalse(Solution().isMatch(s, p))

    def test_2(self):
        s = "aa"
        p = "*"
        self.assertTrue(Solution().isMatch(s, p))

    def test_3(self):
        s = "cb"
        p = "?a"
        self.assertFalse(Solution().isMatch(s, p))

    def test_4(self):
        s = "adceb"
        p = "*a*b"
        self.assertTrue(Solution().isMatch(s, p))

    def test_5(self):
        s = "acdcb"
        p = "a*c?b"
        self.assertFalse(Solution().isMatch(s, p))


if __name__=='__main__':
    unittest.main()
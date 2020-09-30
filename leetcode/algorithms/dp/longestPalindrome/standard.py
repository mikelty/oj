import unittest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2:
            return s
        dp=dict()
        for i in range(len(s)):
            dp[(i,i)]=True
            if i<len(s)-1:
                dp[(i,i+1)]=s[i]==s[i+1]
        for l in range(3,len(s)+1):
            for i in range(len(s)-l+1):
                dp[(i,i+l-1)]=s[i]==s[i+l-1] and dp[(i+1,i+l-2)]
        best,ans=1,s[0]
        for i,j in dp.keys():
            if dp[(i,j)] and j-i+1>best:
                best=max(best,j-i+1)
                ans=s[i:j+1]
        return ans


class MyTest(unittest.TestCase):
    def test_1(self):
        s = "babad"
        ans = "bab"
        self.assertEqual(Solution().longestPalindrome(s),ans)

    def test_2(self):
        s = "cbbd"
        ans = "bb"
        self.assertEqual(Solution().longestPalindrome(s),ans)


if __name__=='__main__':
    unittest.main()
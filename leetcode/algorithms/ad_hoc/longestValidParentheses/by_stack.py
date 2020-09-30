import unittest


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n,res,st=len(s),0,[]
        for i in range(n):
            if s[i]=='(':
                st.append(i)
            elif st and s[st[-1]]=='(':
                st.pop()
            else:
                st.append(i)
        if not st:
            return n
        else:
            a,b=n,0
            while st:
                b=st.pop()
                res=max(res,a-b-1)
                a=b
            return max(res,a)


class MyTest(unittest.TestCase):
    def test_1(self):
        s = "(()"
        self.assertFalse(Solution().longestValidParentheses(s))

    def test_2(self):
        s = ")()())"
        self.assertTrue(Solution().longestValidParentheses(s))


if __name__=='__main__':
    unittest.main()
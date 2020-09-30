class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp=dict()
        for i in range(len(s)):
            for j in range(len(p)):
                if i==0:
                    dp[(i,j)]=False
                    if j==0 and p[j] in ('.',s[i]):
                        dp[(i,j)]=True
                    if p[j]
                elif p[j]=='*':

                    dp[(i,j)]=dp[(i-1,j)] and s[i-1]==s[i]
                    print(i, j,dp[(i,j)])
                elif j>0:
                    dp[(i,j)]=dp[(i-1,j-1)] and p[j] in ('.',s[i])
                else: #i>0, j=0, p[j]!='*'
                    dp[(i,j)]=False
        print(dp)
        return dp[(len(s)-1,len(p)-1)]

sln_obj=Solution()
s = "aa"
p = "a"
assert sln_obj.isMatch(s,p)==False
s = "aa"
p = "a*"
assert sln_obj.isMatch(s,p)==True
s = "ab"
p = ".*"
assert sln_obj.isMatch(s,p)==True
s = "aab"
p = "c*a*b"
assert sln_obj.isMatch(s,p)==True
s = "mississippi"
p = "mis*is*p*."
assert sln_obj.isMatch(s,p)==False
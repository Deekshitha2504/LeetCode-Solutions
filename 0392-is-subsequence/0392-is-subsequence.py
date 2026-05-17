class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p=0
        for i in range(len(t)):
            if p<len(s) and s[p]==t[i]:
                p+=1
        
        return p==len(s)
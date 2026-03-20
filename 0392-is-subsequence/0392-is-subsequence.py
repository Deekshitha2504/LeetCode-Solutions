class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pt1=0
        for i in range(len(t)):
            if pt1<len(s) and s[pt1]==t[i]:
                pt1+=1
        
        return pt1==len(s)
                   
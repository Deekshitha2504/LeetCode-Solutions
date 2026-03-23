class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1=[]
        s2=[]
        for x in s:
            if x=='#':
                if not s1: continue
                s1.pop()
            else:
                s1.append(x)
        for y in t:
            if y=='#':
                if not s2: continue
                s2.pop()
            else:
                s2.append(y)
        return s1==s2                    
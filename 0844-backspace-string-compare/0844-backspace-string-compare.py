class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def check(s):
            stack=[]
            for char in s:
                if char=='#':
                    if not stack: continue
                    stack.pop()
                else:
                    stack.append(char)
            return stack        
        return check(s)==check(t)                    
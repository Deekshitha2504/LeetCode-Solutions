class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ref={'}':'{',')':'(',']':'['}
        stack=[]
        for x in s:
            if x in ref:
                if not stack or stack.pop()!=ref[x]: 
                    return False
            else:
                stack.append(x)
        return not stack    
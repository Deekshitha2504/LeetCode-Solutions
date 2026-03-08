class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        ref={'(':')','[':']','{':'}'}
        for char in s:
            if char in ref.keys():
                stack.append(char)
            else:
                if not stack:
                    return False
                popped=stack.pop()
                if ref[popped]!=char:
                    return False     
        return not stack
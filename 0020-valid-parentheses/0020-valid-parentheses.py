class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        ref={')':'(',']':'[','}':'{'}
        for char in s:
            if char in ref:
                popped=stack.pop() if stack else '#'
                if ref[char]!=popped:
                    return False  
            else:
                stack.append(char)
        return not stack
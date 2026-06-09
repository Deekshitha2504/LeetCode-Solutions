class Solution:
    def isValid(self, s: str) -> bool:
        mapp={')':'(',']':'[','}':'{'}
        stack=[]
        for b in s:
            if b not in mapp:
                stack.append(b)
            else:
                if not stack or mapp[b]!=stack.pop():
                    return False
        return not stack 

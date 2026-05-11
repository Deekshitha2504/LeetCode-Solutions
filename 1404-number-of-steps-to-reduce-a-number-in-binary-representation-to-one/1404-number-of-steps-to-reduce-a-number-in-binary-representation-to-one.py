class Solution:
    def numSteps(self, s: str) -> int:
        carry=0
        count=0
        for i in range(len(s)-1, 0, -1):
            digit=int(s[i])
            if digit+carry==1:
                carry=1
                count+=2
            else:
                count+=1
        return count+carry 
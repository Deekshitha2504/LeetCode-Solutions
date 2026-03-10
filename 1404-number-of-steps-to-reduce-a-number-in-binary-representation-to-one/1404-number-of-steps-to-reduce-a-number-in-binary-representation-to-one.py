class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        dec=int(s,2)
        count=0
        while dec!=1:
           if dec%2==0:
              dec=dec/2
              count+=1
           else:
              dec=dec+1
              count+=1
        return count
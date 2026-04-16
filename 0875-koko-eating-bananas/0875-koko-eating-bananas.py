class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l,r=1,max(piles)
        while l<r:
            k=(l+r)//2
            ttime=0
            for p in piles:
                ttime+=((p+k-1)//k)
            if ttime<=h:
                r=k
            else:
                l=k+1
        return l                
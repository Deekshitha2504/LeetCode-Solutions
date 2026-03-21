class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low=1
        high=x
        ans=0
        while low<=high:
            mid=low+(high-low)//2
            if mid**2==x:
                return mid
            elif mid**2<x:
                ans=mid
                low=mid+1
            elif mid**2>x:
                high=mid-1
        return ans                
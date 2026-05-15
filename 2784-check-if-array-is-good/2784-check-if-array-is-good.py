class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # hashmapp={}
        # n=max(nums)
        # if len(nums)!=n+1:
        #     return False
        # for num in nums:
        #     if num not in hashmapp:
        #         hashmapp[num]=1 
        #     else:
        #         if num!=n:
        #             return False
        #         hashmapp[num]+=1

        # if hashmapp[n]!=2:
        #     return False
        # return True             

        n=len(nums)-1
        hashmapp={}
        if n<=0: return False
        for num in nums:
            hashmapp[num]=hashmapp.get(num,0)+1
        for i in range(1,n):
            if hashmapp.get(i)!=1:
                return False
        return hashmapp.get(n)==2            
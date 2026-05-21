class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # res=[]
        # for num in nums:
        #     count=0
        #     for i in nums:
        #         if i<num:
        #             count+=1
        #     res.append(count)
        # return res         

        mapp={}   
        snums=sorted(nums)
        for i,num in enumerate(snums):
            if num not in mapp:
                mapp[num]=i
        return [mapp[num] for num in nums]        
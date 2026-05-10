class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        longest=0
        for num in s:
            if num-1 not in s:
                curnum=num
                curstreak=1

                while curnum+1 in s:
                    curnum+=1
                    curstreak+=1
                longest=max(longest,curstreak)
        return longest            
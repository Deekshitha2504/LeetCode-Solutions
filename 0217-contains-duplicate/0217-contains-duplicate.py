class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapp={}
        for num in nums:
            if num in mapp:
                return True
            else:
                mapp[num]=1
        return False            
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # l,h=0,len(nums)-1
        # res=[]
        # def bs(l,h):
        #     if l<=h:
        #         mid=(l+h)//2
        #         if nums[mid]==target:
        #             res.append(mid)
        #             bs(l,mid-1)
        #             bs(mid+1,h)
        #         elif nums[mid]<target:
        #             bs(mid+1,h)
        #         else: 
        #             bs(l,mid-1)  
        # bs(l,h)
        # return sorted(res)                 
        def bs(x):
            l,h=0,len(nums)-1
            bound=-1
            while l<=h:
                mid=(l+h)//2
                if nums[mid]==target:
                    bound=mid
                    if x=='left':
                        h=mid-1
                    else:
                        l=mid+1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    h=mid-1
            return bound
        s=bs('left')
        e=bs('right')
        return [s,e]                            
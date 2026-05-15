class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[]
        def bs(x):
            l,r=0,len(nums)-1
            bound=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    bound=mid
                    if x=='l':
                        r=mid-1
                    else:
                        l=mid+1    
                elif nums[mid]<target:  
                    l=mid+1
                else:
                    r=mid-1
            return bound         
        res.append(bs('l'))
        res.append(bs('r'))
        return res
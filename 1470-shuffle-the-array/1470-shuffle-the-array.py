class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # s,f=0,n
        # l=[]
        # count=1
        # while f<=(2*n)-1:
        #     if count%2==0:
        #         l.append(nums[f])
        #         f+=1
        #     else:
        #         l.append(nums[s])  
        #         s+=1
        #     count+=1    
        # return l          

        l=[]
        for i in range(n):
            l.append(nums[i])
            l.append(nums[i+n])
        return l    
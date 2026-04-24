class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp=Counter(nums)
        s=list(mapp.items())
        s.sort(key= lambda x:x[1], reverse=True)
        res=[]            
        for x in range(k):
            res.append(s[x][0])
        return res    
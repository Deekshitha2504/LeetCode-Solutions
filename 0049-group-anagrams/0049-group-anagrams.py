class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for word in strs:
            s="".join(sorted(word))
            if s not in res:
                res[s]=[]
            res[s].append(word)
        return list(res.values())    

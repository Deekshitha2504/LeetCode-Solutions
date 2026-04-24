class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapp={}
        for word in strs:
            s2="".join(sorted(word))
            if s2 not in mapp:
                mapp[s2]=[]
            mapp[s2].append(word)    
        return list(mapp.values())    
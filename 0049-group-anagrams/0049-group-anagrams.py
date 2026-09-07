class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapp={}
        for word in strs:
            s="".join(sorted(word))
            if s not in mapp:
                mapp[s]=[word]
            else:    
                mapp[s].append(word)
        return list(mapp.values())        
class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        count=0
        mapp=set(word)
        for char in mapp:
            if char.islower() and char.upper() in mapp:
                count+=1        
        return count             
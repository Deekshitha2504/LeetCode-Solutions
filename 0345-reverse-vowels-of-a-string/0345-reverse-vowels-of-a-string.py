class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels=['a','e','i','o','u','A','E','I','O','U']
        sl=list(s)
        l,r=0,len(sl)-1
        while l<=r:
            if sl[l] in vowels and sl[r] in vowels:
                sl[l],sl[r]=sl[r],sl[l]
                l+=1
                r-=1
            elif sl[l] in vowels and sl[r] not in vowels:
                r-=1
            elif sl[l] not in vowels and sl[r] in vowels:
                l+=1
            else:
                l+=1
                r-=1    
        return "".join(sl)            
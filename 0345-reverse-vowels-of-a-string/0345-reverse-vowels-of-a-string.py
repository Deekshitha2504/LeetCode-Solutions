class Solution:
    def reverseVowels(self, s: str) -> str:
        l,r=0,len(s)-1
        ref=['A','a','E','e','I','i','O','o','U','u']
        s1=list(s)
        while l<r:
            if s1[l] in ref and s1[r] in ref:
                s1[l],s1[r]=s1[r],s1[l]
                l+=1
                r-=1
            if s1[l] not in ref:
                l+=1
            if s1[r] not in ref:
                r-=1    
        return ''.join(s1)        
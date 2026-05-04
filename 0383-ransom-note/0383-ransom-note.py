class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
       count= Counter(magazine)
       for x in ransomNote:
        if x not in count:
            return False
        elif x in count:
            if count[x]==0:
                return False
            count[x]-=1
       return True          
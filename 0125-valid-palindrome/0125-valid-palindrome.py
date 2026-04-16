class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1=""
        for x in s:
            if x.isalnum():
                s1+=x.lower()
        return s1==s1[::-1]        

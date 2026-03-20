class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res=[]
        a1=len(a)-1
        b2=len(b)-1
        carry=0
        while a1>=0 or b2>=0 or carry:
            total=carry
            if a1>=0:
                total+=int(a[a1])
                a1-=1
            if b2>=0:
                total+=int(b[b2])
                b2-=1
            res.append(str(total%2))
            carry=total//2
        return "".join(reversed(res))            
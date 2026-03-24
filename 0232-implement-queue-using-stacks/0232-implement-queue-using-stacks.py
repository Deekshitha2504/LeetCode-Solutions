class MyQueue(object):

    def __init__(self):
        self.stackA=[]
        self.stackB=[]


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stackA.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if not self.stackB:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
        return self.stackB.pop()               

    def peek(self):
        """
        :rtype: int
        """
        if not self.stackB:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
        return self.stackB[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stackA and not self.stackB


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
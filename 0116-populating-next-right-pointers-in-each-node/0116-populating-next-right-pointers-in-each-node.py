"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return root
        que=deque([root])
        while que:
            size=len(que)
            for x in range(size):
                node=que.popleft()
                node.next=que[0] if x<size-1 else None
                if node.left:que.append(node.left)
                if node.right:que.append(node.right)
        return root  
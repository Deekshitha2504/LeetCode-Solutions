# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root: return []
        result=[]
        que=deque([root])
        while que:
            size=len(que)
            curlvl=[]
            for x in range(size):
                node= que.popleft()
                curlvl.append(node.val)
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
                if x==(size-1):
                    result.append(node.val)
        return result            
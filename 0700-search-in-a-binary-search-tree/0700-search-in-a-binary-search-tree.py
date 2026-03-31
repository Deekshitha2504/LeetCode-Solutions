# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        rot=root
        while rot:
            if rot.val==val:
                return rot
            elif rot.val>val:
                rot=rot.left
            else:
                rot=rot.right

        return None
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a = []
        self.inorder(root, a)
        return a
        
    def inorder(self, curr, l):
        if curr is None:
            return 

        self.inorder(curr.left, l)
        l.append(curr.val)
        self.inorder(curr.right, l)


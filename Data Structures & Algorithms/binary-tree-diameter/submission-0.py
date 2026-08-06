# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0 

        return self.dfs(root.left) + self.dfs(root.right)

    def dfs(self, root):
        if root == None:
            return 0 

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        return max(left, right) + 1


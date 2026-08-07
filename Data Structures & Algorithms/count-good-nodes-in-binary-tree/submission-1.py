# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)


    def dfs(self, root, m):
        if root == None:
            return 0

        good = 0

        if m <= root.val:
            good = 1
        m = max(m, root.val)
        
        return good + self.dfs(root.left, m) + self.dfs(root.right, m)

        
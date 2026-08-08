# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
    
        def dfs(root):
            nonlocal total
            if root == None:
                return
            
            if root.val <= high and root.val >= low:
                total += root.val

            if root.val > high:
                dfs(root.left)
            elif root.val < low:
                dfs(root.right)
            else:
                dfs(root.right)
                dfs(root.left)

        dfs(root)

        return total
                


        
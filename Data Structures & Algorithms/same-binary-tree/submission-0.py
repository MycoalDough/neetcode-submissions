# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p,q)
        

    def dfs(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        if (node1 == None and node2 != None) or (node2 == None and node1 != None) or (node1.val != node2.val):
            return False
        if node1.val == node2.val:
            left = self.dfs(node1.left, node2.left)
            right = self.dfs(node1.right, node2.right)
            return left and right



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return 

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            #delete
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            ss = root.right
            while ss.left:
                ss = ss.left
            
            root.val = ss.val

            root.right = self.deleteNode(root.right, ss.val)

        return root
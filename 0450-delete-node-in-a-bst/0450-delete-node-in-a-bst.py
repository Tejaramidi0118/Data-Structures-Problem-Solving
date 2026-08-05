# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def inOrderSucc(root):
            while root and root.left:
                root = root.left
            
            return root

        def delNode(root,val):
            if not root:
                return None 

            if root.val > val:
                root.left = delNode(root.left,val)
            elif root.val < val:
                root.right = delNode(root.right,val)
            else:
                if not root.left:
                    return root.right
                
                if not root.right:
                    return root.left
                
                succ = inOrderSucc(root.right)
                root.val = succ.val
                root.right =  delNode(root.right,succ.val)

            return root

        return delNode(root,key)

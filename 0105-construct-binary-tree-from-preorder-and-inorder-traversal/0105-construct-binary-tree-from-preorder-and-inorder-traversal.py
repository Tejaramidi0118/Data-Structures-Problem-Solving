# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def l_and_r(arr, i):
            left = None
            right = None

            x = -1
            for a, b in enumerate(arr):
                if b == i:
                    x = a
                    break  

            if x != -1 and x in range(0, len(arr)):
                left = arr[:x]
                right = arr[x+1:]

            return left, right
        
        def build(inorder):
            if not inorder:
                return None
            
            if not preorder:
                return None

            node = preorder.pop(0)
            tree = TreeNode(node)

            left_subT, right_subT = l_and_r(inorder, node)

            tree.left = build(left_subT)
            tree.right = build(right_subT)

            return tree
        
        return build(inorder)

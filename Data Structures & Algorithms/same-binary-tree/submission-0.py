# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res1=[]
        res2=[]
        def preorder(node,res):
            if node==None:
                res.append(None)
                return
            res.append(node.val)
            preorder(node.left,res)
            preorder(node.right,res)
        preorder(p,res1)
        preorder(q,res2)
        print(res1)
        print(res2)
        if res1==res2:
            return True
        return False
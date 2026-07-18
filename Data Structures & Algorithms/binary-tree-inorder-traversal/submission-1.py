# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        curr=root
        while(curr!=None):
            if curr.left==None:
                res.append(curr.val)
                curr=curr.right
            else:
                leftChild=curr.left
                while leftChild.right is not None and leftChild.right != curr:
                    leftChild = leftChild.right
                leftChild.right = curr
                temp=curr
                curr=curr.left
                temp.left=None       
        return res
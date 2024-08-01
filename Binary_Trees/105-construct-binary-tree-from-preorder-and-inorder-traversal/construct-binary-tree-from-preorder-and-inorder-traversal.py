# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inMap = {val:idx for idx, val in enumerate(inorder)}

        root = self.makeTree(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, inMap)

        return root

    def makeTree(self, preorder, preStart, preEnd, inorder, inStart, inEnd, inMap):

        if preStart > preEnd or inStart > inEnd:
            return None
        
        root = TreeNode(preorder[preStart])

        rootIndex = inMap[root.val]

        numsleft = rootIndex - inStart

        root.left = self.makeTree(preorder, preStart + 1, preStart + numsleft, inorder, inStart, rootIndex-1, inMap)

        root.right = self.makeTree(preorder, preStart + numsleft + 1, preEnd, inorder, rootIndex+1, inEnd, inMap)

        return root


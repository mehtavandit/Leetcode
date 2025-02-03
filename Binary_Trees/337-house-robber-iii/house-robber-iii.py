# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        #will return pairs of withRoot and withoutRoot

        def dfs (node):

            if node is None:
                return (0,0)

            lsid = dfs(node.left)
            rsid = dfs(node.right)

            withRoot = node.val + lsid[1] + rsid[1]
            withoutRoot = max(lsid) + max(rsid)

            return (withRoot, withoutRoot)

        return max(dfs(root))


            
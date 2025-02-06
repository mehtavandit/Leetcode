# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def generate_trees(start, end):

            if (start, end) in memo:
                return memo[(start, end)]

            trees = []
            if start > end:
                trees.append(None)
                return trees

            for root in range(start, end + 1):
                left_subtree = generate_trees(start, root-1)
                right_subtree = generate_trees(root+1, end)

                for left in left_subtree:
                    for right in right_subtree:
                        nn = TreeNode(root, left, right)
                        trees.append(nn)

                memo[(start, end)] = trees
            
            return trees
        
        if n == 0:
            return []
            
        memo = {}
        return generate_trees(1, n)

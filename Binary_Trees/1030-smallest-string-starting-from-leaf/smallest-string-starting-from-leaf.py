# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.base = 97
        self.smallest_string = None

        def dfs(root, path):
            if root is None:
                return

            path.append(chr(97 + root.val))

            if root.left is None and root.right is None:
                reversed_path = "".join(reversed(path))
                if self.smallest_string is None:
                    self.smallest_string = reversed_path
                else:
                    self.smallest_string = min(self.smallest_string, reversed_path)
                

            dfs(root.left, path)
            dfs(root.right, path)

            path.pop()

            
        dfs(root, [])
        return self.smallest_string
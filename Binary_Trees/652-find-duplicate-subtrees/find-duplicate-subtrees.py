# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtree_info = defaultdict(list)
        result = []
        seen = set()

        def serialize(node):
            if not node:
                return "null"

            lefts = serialize(node.left)
            rights = serialize(node.right)

            string = f"{node.val}({lefts})({rights})"
            print(string)

            if string in subtree_info:
                if string not in seen:  
                    result.append(subtree_info[string])
                    seen.add(string)
            else:
                subtree_info[string] = node

            return string

        serialize(root)
        return result
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        queue = deque([root])
        level_sums = []

        while queue:
            level_sum = 0
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_sums.append(level_sum)

        queue = deque([root])
        root.val = 0
        level_index = 1

        while queue:
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()

                left_child_sum = node.left.val if node.left else 0
                right_child_sum = node.right.val if node.right else 0

                sibling_sum = left_child_sum + right_child_sum

                if node.left:
                    node.left.val = level_sums[level_index] - sibling_sum
                    queue.append(node.left)

                if node.right:
                    node.right.val = level_sums[level_index] - sibling_sum
                    queue.append(node.right)

            level_index += 1

        return root
from collections import deque
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if root is None:
            return []

        def build_parent_map(root):
            parent_map = {}
            
            def dfs(node, parent):
                if not node:
                    return
                if parent:
                    parent_map[node] = parent
                dfs(node.left, node)
                dfs(node.right, node)
                
            dfs(root, None)
            return parent_map

        def find_target(node, target):
            if node is None:
                return None
            if node.val == target.val:
                return node
            left = find_target(node.left, target)
            if left:
                return left
            return find_target(node.right, target)

        # Locate the target node by its value
        target_node = find_target(root, target)

        if target_node is None:
            return []

        # Create a map to find parents of each node
        parent_map = build_parent_map(root)

        # BFS to find all nodes at distance k from the target node
        queue = deque([(target_node, 0)])
        visited = {target_node}
        result = []

        while queue:
            node, distance = queue.popleft()

            if distance == k:
                result.append(node.val)
            elif distance < k:
                # Check the left child
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append((node.left, distance + 1))
                # Check the right child
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append((node.right, distance + 1))
                # Check the parent
                parent = parent_map.get(node)
                if parent and parent not in visited:
                    visited.add(parent)
                    queue.append((parent, distance + 1))

        return result

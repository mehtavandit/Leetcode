# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.result = []
        self.inorder(root)
        # print(self.result)
        self.pointer = -1
        self.length = len(self.result)

    def next(self) -> int:
        if self.hasNext:
            self.pointer += 1
            return self.result[self.pointer]

    def hasNext(self) -> bool:
        if self.pointer < self.length - 1:
            return True
        return False
    
    def inorder(self, node):
        if node is None:
            return
        
        self.inorder(node.left)

        self.result.append(node.val)

        self.inorder(node.right)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
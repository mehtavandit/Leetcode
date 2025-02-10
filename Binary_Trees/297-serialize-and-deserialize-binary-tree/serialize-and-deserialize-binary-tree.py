# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        result = []

        def preorder(root):
            if root is None:
                result.append("N")
                return
            
            result.append(str(root.val))

            preorder(root.left)

            preorder(root.right)

        
        preorder(root)
        return ",".join(result)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        data = data.split(",")
        def generate_tree():
            val = data.pop(0)
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = generate_tree()
            node.right = generate_tree()
            return node

        return generate_tree()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
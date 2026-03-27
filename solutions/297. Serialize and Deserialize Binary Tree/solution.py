# Problem: Serialize and Deserialize Binary Tree
# Language: python3
# Runtime: 112 ms
# Memory: 22.2 MB

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
        self.A = []
        def walk(node):
            if node:
                self.A.append(str(node.val))
                walk(node.left)
                walk(node.right)
            else:
                self.A.append('')
        walk(root)
        return ",".join(self.A)
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def walk(A):
            val = A.pop()
            if not val:
                return None
            node = TreeNode(int(val))
            node.left = walk(A)
            node.right = walk(A)
            return node
        
        return walk(data.split(",")[::-1])
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
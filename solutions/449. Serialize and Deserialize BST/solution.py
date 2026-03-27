# Problem: Serialize and Deserialize BST
# Language: python3
# Runtime: 76 ms
# Memory: 18 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
from math import inf

class Codec:
    def __init__(self):
        self.str = ""
        self.tree = None
    
    def _inorder(self, root):
        if root:                
            self._inorder(root.left)
            
            s = str(root.val)
            if self.str:
                self.str += "," + s
            else:
                self.str = s            
            self._inorder(root.right)

    def _postorder(self, root):
        if root:                
            
            

            self._postorder(root.left)
            self._postorder(root.right)
            s = str(root.val)
            if self.str:
                self.str += "," + s
            else:
                self.str = s
    
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """

        self.str = ""
        self._postorder(root)
        return self.str
    
 
            
    
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if data == "":
            return []
        

        postorder  = list(map(int,data.split(",")))
        

        def convert2tree(lower = -inf, upper = inf):
            if not postorder or postorder[-1] < lower or postorder[-1] > upper:
                return None
            
            val = postorder.pop()
            node = TreeNode(val)
            node.right = convert2tree(val, upper)
            node.left  = convert2tree(lower, val)
            
            
            
            return node
            
        #convert2tree(0, len(l)-1)
        return convert2tree()

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
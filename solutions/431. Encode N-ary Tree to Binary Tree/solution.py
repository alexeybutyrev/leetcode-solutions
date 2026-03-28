# Problem: Encode N-ary Tree to Binary Tree
# Language: python3
# Runtime: 143 ms
# Memory: 18.1 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        def walk(node, direction = "right"):
            if node:
                tree = TreeNode(node.val)
                r = tree
                if direction == "right":
                    for c in node.children:
                        r.right = walk(c, direction = "left")
                        r = r.right
                else:
                    for c in node.children:
                        r.left = walk(c, direction = "right")
                        r = r.left
                    
                return tree
            else:
                return None

        return walk(root)
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        def walk(node, direction = "right"):
            if node:
                tree = Node(node.val, [])
                if direction == "right":
                    r = node.right
                    while r:
                        c = walk(r, direction = "left")
                        tree.children.append(c)
                        r = r.right
                else:
                    
                    r = node.left
                    while r:
                        c = walk(r, direction = "right")
                        tree.children.append(c)
                        r = r.left
                return tree
            else:
                return None
        return walk(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
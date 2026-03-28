# Problem: Serialize and Deserialize N-ary Tree
# Language: python3
# Runtime: 92 ms
# Memory: 17 MB

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:

        res = []
        def recursive(node):
            if not node:return
            res.append(str(node.val))
            for n in node.children:
                recursive(n)
            res.append('#')
        recursive(root)
        return ','.join(res)           
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:return
        data = data.split(',')
        root = Node(int(data[0]),[])
        stack = [root]
        for i in data[1:]:
            if i == '#':
                node = stack.pop()
                if stack:
                    stack[-1].children.append(node)
            else:
                new = Node(int(i),[])
                stack.append(new)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
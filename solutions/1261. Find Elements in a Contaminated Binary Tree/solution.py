# Problem: Find Elements in a Contaminated Binary Tree
# Language: python3
# Runtime: 92 ms
# Memory: 18.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.elements = set()
        def walk(node, val):
            if node:
                self.elements.add(val)
                node.val = val
                node.left  = walk(node.left, 2 * val + 1)
                node.right = walk(node.right, 2 * val + 2)
                return node
            else:
                return None
        self.tree = walk(root,0)
        

    def find(self, target: int) -> bool:
        return target in self.elements


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
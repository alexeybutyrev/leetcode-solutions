# Problem: Binary Search Tree Iterator
# Language: python3
# Runtime: 72 ms
# Memory: 21 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = [root]
        
        
        def walk(node):
            if node:
                left = walk(node.left)
                right = walk(node.right)
                return right + [node.val] + left
            else:
                return []
        
        self.array = walk(root)
            
    def next(self) -> int:
        return self.array.pop()
        """
        if self.hasNext():
            node = self.stack.pop()
            if node.right:
                self.stack.append(node.right)
            if node.left:
                self.stack.append(node.left)
                
            return node.val
        else:
            return None
        """         
                

    def hasNext(self) -> bool:
        if self.array:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
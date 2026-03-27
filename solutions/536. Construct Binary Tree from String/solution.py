# Problem: Construct Binary Tree from String
# Language: python3
# Runtime: 284 ms
# Memory: 15.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if s:
            num = ""
            for i,l in enumerate(s):
                if l == "(":
                    break
                else:
                    num += l
            else:
                return TreeNode(int(num))

            node = TreeNode(int(num))

            N = len(s)

            left_p = 1
            right_p = 0
            left_string = ""
            for i in range(i+1, N):
                l = s[i]
                if l == "(":
                    left_p += 1
                elif l == ")":
                    right_p += 1
                    if right_p == left_p:
                        break

                left_string += l

            node.left = self.str2tree(left_string)

            if i < N - 1:

                left_p = 1
                right_p = 0
                right_string = ""
                for i in range(i+2, N):
                    l = s[i]
                    if l == "(":
                        left_p += 1
                    elif l == ")":
                        right_p += 1
                        if right_p == left_p:
                            break

                    right_string += l
                node.right = self.str2tree(right_string)

            return node
        else:
            return None

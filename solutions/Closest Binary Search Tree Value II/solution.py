# Problem: Closest Binary Search Tree Value II
# Language: python3
# Runtime: 54 ms
# Memory: 18.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], t: float, k: int) -> List[int]:
        h = []
        def walk(node):
            if node:
                if len(h) < k:
                    heappush(h, (-abs(node.val -t),node.val))
                else:
                    t1,v1 = heappop(h)
                    t2,v2 = -abs(node.val -t),node.val
                    if t1 <= t2:
                        heappush(h,(t2,v2))
                    else:
                        heappush(h,(t1,v1))
                walk(node.left)
                walk(node.right)
        walk(root)
        ans = []
        while h:
            ans.append(heappop(h)[1])
        return ans
# Problem: Maximum Total Subarray Value II
# Language: python3
# Runtime: 11119 ms
# Memory: 74.5 MB

class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.sum = 0
        self.min = inf
        self.max = -inf
        
class FenwichTree:
    def __init__(self, arr):
        self.root = self.buildTree(arr, 0, len(arr)-1)
        
    def buildTree(self, arr, l, r):
        if l > r: return None
        root = TreeNode(l, r)
        if l == r:  root.sum = root.min = root.max = arr[l];  return root
        m = l + (r - l) // 2
        root.left = self.buildTree(arr, l, m)
        root.right = self.buildTree(arr, m+1, r)
        root.sum = root.left.sum + root.right.sum
        root.min = min(root.left.min, root.right.min)
        root.max = max(root.left.max, root.right.max)
        return root
        
    def update(self, index, val, node=None):
        if node is None: node = self.root
        if node.start == node.end: node.sum = val; return 
        m = node.start + (node.end - node.start) // 2
        if index <= m: self.update(index, val, node.left)
        else: self.update(index, val, node.right)
        node.sum = node.left.sum + node.right.sum
        node.min = min(node.left.min, node.right.min)
        node.max = max(node.left.max, node.right.max)
        
    def sumRange(self, st, end, node=None):
        if node is None: node = self.root
        if node.start == st and node.end == end: return node.sum
        m = node.start + (node.end - node.start) // 2
        if end <= m: return self.sumRange(st, end, node.left)
        if st >= m+1: return self.sumRange(st, end, node.right)
        return self.sumRange(st, m, node.left) + self.sumRange(m+1, end, node.right)
    
    def minRange(self, st, end, node=None):
        if node is None: node = self.root
        if node.start == st and node.end == end: return node.min
        m = node.start + (node.end - node.start) // 2
        if end <= m: return self.minRange(st, end, node.left)
        if st >= m+1: return self.minRange(st, end, node.right)
        return min(self.minRange(st, m, node.left), self.minRange(m+1, end, node.right))
    
    def maxRange(self, st, end, node=None):
        if node is None: node = self.root
        if node.start == st and node.end == end: return node.max
        m = node.start + (node.end - node.start) // 2
        if end <= m: return self.maxRange(st, end, node.left)
        if st >= m+1: return self.maxRange(st, end, node.right)
        return max(self.maxRange(st, m, node.left), self.maxRange(m+1, end, node.right))


class Solution:
    def maxTotalValue(self, A: List[int], k: int) -> int:
        T = FenwichTree(A)
        q = []
        N = len(A)
        mm = T.minRange(0,N-1) - T.maxRange(0,N-1)
        heappush(q,(mm,0,N-1))
        ans = 0
        seen = {(0,N-1)}
        while q and k:
            d,l,r = heappop(q)
            ans -= d
            k -= 1
            if not k: return ans

            if (l+1,r) not in seen and l+1 < r:
                seen.add((l+1,r))
                mm = T.minRange(l+1,r)-T.maxRange(l+1,r)
                heappush(q,(mm,l+1,r))

            if (l,r-1) not in seen and l < r-1:
                seen.add((l,r-1))
                mm = T.minRange(l,r-1)-T.maxRange(l,r-1)
                heappush(q,(mm,l,r-1))
            
        return ans
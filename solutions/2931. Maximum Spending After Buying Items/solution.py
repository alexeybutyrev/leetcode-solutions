# Problem: Maximum Spending After Buying Items
# Language: python3
# Runtime: 973 ms
# Memory: 35.1 MB

class Solution:
    def maxSpending(self, A: List[List[int]]) -> int:
        
        
        h = []
        B = Counter()
        for a in A:
            B += Counter(a)
        count = 0
        ans = 0
        for k in sorted(B.keys()):
            v = B[k]
            c = v * (v + 1) // 2
            ans += k * (count * v + c)
            count += v
        return ans
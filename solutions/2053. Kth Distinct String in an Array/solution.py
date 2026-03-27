# Problem: Kth Distinct String in an Array
# Language: python3
# Runtime: 72 ms
# Memory: 14.5 MB

class Solution:
    def kthDistinct(self, A: List[str], k: int) -> str:
        s = set()
        c = Counter()
        for a in A:
            
            c[a] += 1
        for a in A:
            if c[a] == 1:
                s.add(a)
            if len(s) == k:
                return a
        return ""
        
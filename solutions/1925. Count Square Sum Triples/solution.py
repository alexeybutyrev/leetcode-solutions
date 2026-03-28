# Problem: Count Square Sum Triples
# Language: python3
# Runtime: 9780 ms
# Memory: 14 MB

class Solution:
    def countTriples(self, n: int) -> int:
        s = set()
        count = 0
        for a in range(1,n+1):
            for b in range(a+1,n+1):
                for c in range(b + 1,n+1):
                    if c * c == a * a + b * b:
                        count += 2
        return count
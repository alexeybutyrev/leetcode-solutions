# Problem: Minimum Index of a Valid Split
# Language: python3
# Runtime: 82 ms
# Memory: 34.7 MB

class Solution:
    def minimumIndex(self, A: List[int]) -> int:
        c = Counter(A)
        kk = max(c.keys(), key = lambda y: c[y])
        
        curr = 0
        for i,x in enumerate(A):
            if x == kk:
                curr += 1
                c[x] -= 1
            
            left = i + 1
            right = len(A) - i-1
            
            if curr * 2 > left and c[kk] * 2 > right:
                return i
        return -1
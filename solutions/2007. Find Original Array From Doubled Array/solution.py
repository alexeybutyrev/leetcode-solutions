# Problem: Find Original Array From Doubled Array
# Language: python3
# Runtime: 2112 ms
# Memory: 33 MB

class Solution:
    def findOriginalArray(self, A: List[int]) -> List[int]:
        N = len(A)
        c = Counter(A)
        ans = []
        for x in sorted(A):
            if c[x]:
                c[x] -= 1
                c[2*x] -= 1
                if c[2*x] < 0:
                    return []
                ans.append(x)
        return ans
    
            
# Problem: Intersection of Two Arrays II
# Language: python3
# Runtime: 41 ms
# Memory: 14.1 MB

class Solution:
    def intersect(self, A: List[int], B: List[int]) -> List[int]:
        if len(A) < len(B):
            B,A = A,B

        cA = Counter(A)
        cB = Counter(B)
        ans = []
        for a in cA:
            if a in cB:
                ans += [a] * min(cA[a],cB[a])
        return ans
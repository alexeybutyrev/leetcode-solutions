# Problem: Divide an Array Into Subarrays With Minimum Cost I
# Language: python3
# Runtime: 3 ms
# Memory: 19.3 MB

class Solution:
    def minimumCost(self, A: List[int]) -> int:
        return A.pop(0) + sum(sorted(A)[0:2])
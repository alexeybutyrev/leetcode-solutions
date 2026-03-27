# Problem: Largest Unique Number
# Language: python3
# Runtime: 44 ms
# Memory: 14.4 MB

class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        c = Counter(A)
        ans = -1
        for k,v in c.items():
            if v == 1 and k > ans:
                ans = k
        return ans
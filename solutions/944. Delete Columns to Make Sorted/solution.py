# Problem: Delete Columns to Make Sorted
# Language: python3
# Runtime: 263 ms
# Memory: 16.2 MB

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        A = []
        for s in strs:
            A.append(list(s))
        ans = 0
        for l in list(zip(*A)):
            x = list(l)
            ans += (x != sorted(x))
        return ans
            
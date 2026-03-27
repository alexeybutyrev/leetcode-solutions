# Problem: Count Pairs Whose Sum is Less than Target
# Language: python3
# Runtime: 56 ms
# Memory: 16.4 MB

class Solution:
    def countPairs(self, A: List[int], target: int) -> int:
        ans = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[i] + A[j] < target:
                    ans += 1
        return ans
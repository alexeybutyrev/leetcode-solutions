# Problem: Longest Balanced Subarray I
# Language: python3
# Runtime: 1225 ms
# Memory: 19.4 MB

class Solution:
    def longestBalanced(self, A: List[int]) -> int:
        ans = 0
        for i in range(N:=len(A)):
            s1 = set()
            s2 = set()
            for j in range(i,N):
                if A[j] & 1:
                    s1.add(A[j])
                else:
                    s2.add(A[j])
                if len(s1) == len(s2): ans = max(ans, j - i + 1)
        return ans
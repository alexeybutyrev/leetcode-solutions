# Problem: Partition Array Such That Maximum Difference Is K
# Language: python3
# Runtime: 1834 ms
# Memory: 28 MB

class Solution:
    def partitionArray(self, A: List[int], k: int) -> int:
        N = len(A)
        if N == 0:
            return 0
        A.sort()
        ans = 0
        mn = mx = A[0]
        for i in range(N):
            mn = min(mn,A[i])
            mx = max(mx,A[i])
            #print(i,ans)
            if mx - mn > k:
                mn = mx = A[i]
                ans += 1
        return ans + 1
        
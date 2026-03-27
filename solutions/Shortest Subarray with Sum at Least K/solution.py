# Problem: Shortest Subarray with Sum at Least K
# Language: python3
# Runtime: 163 ms
# Memory: 33.1 MB

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        q = deque()
        S = list(accumulate(nums,initial = 0))
        ans = inf
        for i,a in enumerate(S):
            while q and a <= S[q[-1]]:
                q.pop()
            
            while q and a - S[q[0]] >= k:
                ans = min(ans, i - q.popleft())
            
            q.append(i)
                
        return -1 if ans == inf else ans
# Problem: Sliding Window Maximum
# Language: python3
# Runtime: 1263 ms
# Memory: 33.2 MB

class Solution:
    def maxSlidingWindow(self, A: List[int], k: int) -> List[int]:
        d = deque()
        for i in range(k-1):
            while d and A[d[-1]]< A[i]:
                d.pop()
            d.append(i)
        ans = []
        for i in range(k-1,len(A)):
            while d and A[d[-1]]< A[i]:
                d.pop()
            d.append(i)
            if len(d) > k or d[-1]-d[0]>=k:
                d.popleft()
            ans.append(A[d[0]])
        return ans

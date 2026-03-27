# Problem: Find the K-Sum of an Array
# Language: python3
# Runtime: 862 ms
# Memory: 30 MB

class Solution:
    def kSum(self, A: List[int], k: int) -> int:
        N = len(A)
        S = sum(a for a in A if a > 0)
        A = [abs(a) for a in A]
        A.sort()
        h = []
        heappush(h,(-S + A[0],0))
        ans = [S]
        
        while len(ans) < k:
            s, i = heappop(h)
            heappush(ans,-s)
            if i < N - 1:
                heappush(h, (s - A[i]+A[i+1],i+1))
                heappush(h, (s + A[i+1],i+1))
        return ans[0]
        
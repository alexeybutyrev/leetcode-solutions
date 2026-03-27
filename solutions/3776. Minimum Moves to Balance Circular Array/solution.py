# Problem: Minimum Moves to Balance Circular Array
# Language: python3
# Runtime: 103 ms
# Memory: 31.8 MB

class Solution:
    def minMoves(self, A: List[int]) -> int:

        if sum(A) < 0: return -1
        L, R = [],[]
        N = len(A)
        
        for mid in range(N):
            if A[mid] < 0:
                break
        else:
            return 0

        if N == 2:
            return -A[mid]

        for i in range(mid+1, mid + N):
            R.append(A[i % N])

        for i in range(mid-1, mid - N, -1):
            L.append(A[i])

        L = L[::-1]
        R = R[::-1]
        s = -A[mid]
        m = 1
        ans = 0
        while L and R:
            l = L.pop()
            r = R.pop()
            
            if l + r < s:
                ans += m * (l + r)
                s -= l
                s -= r
            else:
                left = s
                ans += left * m
                return ans
            m += 1
        return ans
        
        
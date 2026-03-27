# Problem: Count the Number of Good Subarrays
# Language: python3
# Runtime: 861 ms
# Memory: 31.9 MB

class Solution:
    def countGood(self, A: List[int], k: int) -> int:
        c = Counter()
        j = 0
        ans = 0
        N = len(A)
        for i in range(N):
            k -= c[A[i]]
            c[A[i]] += 1
            
            while k <= 0:
                c[A[j]] -= 1
                k += c[A[j]]
                j += 1
            ans += j
        return ans
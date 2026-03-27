# Problem: Count Distinct Subarrays Divisible by K in Sorted Array
# Language: python3
# Runtime: 527 ms
# Memory: 45.5 MB

class Solution:
    def numGoodSubarrays(self, A: List[int], K: int) -> int:
        F = [0]

        for x in A:
            F.append(F[-1] + x)

        N = len(A)
        c = Counter()
        ans = 0
        for i in range(0,N+1):
            ans += c[F[i] % K]
            c[F[i] % K] += 1

        c = Counter(A)

        # for x in c:
        #     if K % x == 0 and c[x] >= K // x:
        #         ans -= (c[x] - K // x)

        for x in c:
            M = c[x]
            for m in range(1,c[x]+1):
                if (m * x) % K == 0:
                    ans -= (M-m)
        
        return ans
# Problem: Count Subarrays With K Distinct Integers
# Language: python3
# Runtime: 273 ms
# Memory: 29.1 MB


class Solution:
    def countSubarrays(self, A: list[int], K: int, M: int) -> int:
        N = len(A)
        
        start1 = start2 = 0
        cM = Counter()
        cK = Counter()

        dist = 0
        cnt = 0

        end = 0
        ans = 0

        while end < N:
            # update maps for end
            if cK[A[end]] == 0: dist += 1
            cK[A[end]] += 1
            cM[A[end]] += 1
            if cM[A[end]] == M: cnt += 1

            # shrik start1 to get till distinct K
            while dist > K:
                cK[A[start1]] -= 1
                if cK[A[start1]] == 0: dist -=1
                start1 += 1
            
            
            while cnt >= K:
                cM[A[start2]] -= 1
                if cM[A[start2]] == M - 1: cnt -=1
                start2 += 1

            # update ans
            if start2 > start1:
                ans += start2 - start1 
            end += 1
            
        return ans

# Problem: Split and Merge Array Transformation
# Language: python3
# Runtime: 315 ms
# Memory: 17.9 MB

class Solution:
    def minSplitMerge(self, A: List[int], B: List[int]) -> int:
        q = deque([tuple(A)])
        seen = set(tuple(A))
        B = tuple(B)
        N = len(A)
        ans = 0
        while q:
            L = len(q)
            for _ in range(L):
                A = q.popleft()
                if A == B: return ans 
                for i in range(N):
                    for j in range(i+1,N+1):
                        L = A[:i]
                        M = A[i:j]
                        R = A[j:]
                        NA = L + R
                        for k in range(len(NA) + 1):
                            C = tuple(NA[:k] + M + NA[k:])
                            if C not in seen:
                                seen.add(C)
                                q.append(C)
                
                    
            ans += 1
        return ans
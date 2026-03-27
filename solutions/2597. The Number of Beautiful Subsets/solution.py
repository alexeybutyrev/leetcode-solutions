# Problem: The Number of Beautiful Subsets
# Language: python3
# Runtime: 4671 ms
# Memory: 16.5 MB

class Solution:
    def beautifulSubsets(self, A: List[int], K: int) -> int:
        N = len(A)
        self.ans = N
        def walk(i, inds):
            if i < N:
                for j in inds:
                    if abs(A[j] - A[i]) == K:
                        break
                else:
                    self.ans += 1
                    walk(i+1, inds + [i])
                walk(i+1,inds)
        
        for i in range(N):
            walk(i+1, [i])
        return self.ans
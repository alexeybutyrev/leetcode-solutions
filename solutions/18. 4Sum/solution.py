# Problem: 4Sum
# Language: python3
# Runtime: 144 ms
# Memory: 18.5 MB

class Solution:
    def fourSum(self, A: List[int], target: int) -> List[List[int]]:
        S = defaultdict(list)
        N = len(A)
        ans = set()
        for i in range(N):
            for j in range(i+1, N):
                S[A[i] + A[j]].append((i,j))
        
        for i in range(N):
            for j in range(i+1, N):
                c = target - A[i] - A[j]
                if c in S:
                    for k,l in S[c]:
                        if k!= i and l!= j and k!=j and l!=i:
                            ans.add(tuple(sorted([A[i],A[j],A[k],A[l]])))

        
        
        
        return ans
        
        
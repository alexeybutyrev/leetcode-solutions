# Problem: Frog Jump
# Language: python3
# Runtime: 457 ms
# Memory: 28.6 MB

class Solution:
    def canCross(self, A: List[int]) -> bool:
        N = len(A)
        seen = {(0,0)}
        q = [(0,0)]
        for s,k in q:
            if s >= N - 1:
                return True
            for x in [k-1,k,k+1]:
                ns = A[s] + x
                ind = bisect_left(A,ns)
                nk = x
                if ind > N-1: continue
                
                if A[ind] == ns and (ind,nk) not in seen:
                    seen.add((ind,nk))
                    q.append((ind,nk))
        return False
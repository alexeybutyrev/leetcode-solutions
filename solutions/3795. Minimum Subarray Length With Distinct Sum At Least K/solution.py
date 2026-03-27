# Problem: Minimum Subarray Length With Distinct Sum At Least K
# Language: python3
# Runtime: 1474 ms
# Memory: 38 MB

class Solution:
    def minLength(self, A: List[int], K: int) -> int:
        c = Counter()
        i = -1
        q = deque()
        s = 0
        ans = inf
        for j,x in enumerate(A):
            q.append(x)
            if x not in c:
                s += x
                if s >= K:
                    ans = min(ans, len(q))
                c[x] += 1
            else:
                c[x] += 1
            
            while (q and ( (s - q[0]) >= K)) or (s >= K and c[q[0]] > 1):
                a = q.popleft()
                if c[a] == 1:
                    s -= a
                c[a] -= 1
                if not c[a]: del c[a]
                
                ans = min(ans, len(q))
                
        return -1 if ans== inf else ans
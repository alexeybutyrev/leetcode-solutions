# Problem: Count Number of Maximum Bitwise-OR Subsets
# Language: python3
# Runtime: 6820 ms
# Memory: 19.9 MB

class Solution:
    def countMaxOrSubsets(self, A: List[int]) -> int:
        d = defaultdict(set)
        N = len(A)
        
        q = deque([(0,0)])
        ans = 0
        used = {0}
        mx = 0
        while q:
            L = len(q)
            for _ in range(L):
                c, mask = q.popleft()
                if c > mx:
                    mx = c
                    ans = 0
                    
                if c == mx:
                    ans += 1
                
                for i in range(N):
                    if mask & (1 << i) == 0 and mask | (1 << i) not in used:
                        used.add(mask | (1 << i))
                        q.append((c | A[i], mask | (1 <<i)))
            
        return ans
    
            
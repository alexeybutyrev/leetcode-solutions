# Problem: Number of People Aware of a Secret
# Language: python3
# Runtime: 526 ms
# Memory: 17.9 MB

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7
        q = deque([[1,1]])
        
        for i in range(1,n):
            while q[0][1] >= forget:
                q.popleft()
            
            for j in range(len(q)):
                q[j][1] += 1
            
            s = 0
            for j in range(len(q)):
                
                if q[j][1] > delay:
                    s += q[j][0]
                    s %= MOD
            if s:
                q.append([s,1])
        
        
        return sum(x for x,_ in q) % MOD
                
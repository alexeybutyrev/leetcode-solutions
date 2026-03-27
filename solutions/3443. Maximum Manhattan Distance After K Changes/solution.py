# Problem: Maximum Manhattan Distance After K Changes
# Language: python3
# Runtime: 2267 ms
# Memory: 18.4 MB

class Solution:
    def maxDistance(self, s: str, K: int) -> int:
        c = Counter(s[:K])
        ans = K
        for d in s[K:]:
            
            c[d] += 1
            a1 = max(c['N'],c['S'])
            a2 = max(c['E'],c['W'])
            m1 = min(c['N'],c['S'])
            m2 = min(c['E'],c['W'])
            k0 = K
            M = m1 + m2
            if M <= K:
                ans = max(ans, a1 + a2 + M)
            else:
                ans = max(ans, a1 + a2 + K - (M - K))

        

        return ans
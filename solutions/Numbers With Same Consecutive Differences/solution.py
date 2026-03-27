# Problem: Numbers With Same Consecutive Differences
# Language: python3
# Runtime: 52 ms
# Memory: 14.2 MB

from collections import deque
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        q = deque()
        for i in range(1,10):
            q.append([i])
        
        for _ in range(N-1):
            l = len(q)
            for i in range(l):
                nums = q.popleft()
                v = nums[-1]
                
                if v - K >= 0:
                    q.append(nums + [v-K])
                
                if v + K <= 9:
                    q.append(nums + [v+K])
                
        if not q:
            return []
        res = list(set(map(lambda x: "".join(map(str,x)),q)))
        if N == 1:
            res = [0] + res
        return res
                    
# Problem: Frequency of the Most Frequent Element
# Language: python3
# Runtime: 1193 ms
# Memory: 30.5 MB

class Solution:
    def maxFrequency(self, A: List[int], k: int) -> int:
        A.sort(reverse=True)
        q = deque([A[0]])
        ans = 1
        for x in A[1:]:
            if q[0] - x > k:
                
                while q and q[0] - x> k:
                    y = q.popleft()
                    if q:
                        l = len(q)
                        delta = y -q[0]
                        k += delta * l
            if q:
                k-=q[0]-x
            q.append(x)
            
            ans = max(ans,len(q))
        return ans
                    
            
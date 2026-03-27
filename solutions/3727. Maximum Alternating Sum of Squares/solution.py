# Problem: Maximum Alternating Sum of Squares
# Language: python3
# Runtime: 183 ms
# Memory: 31.7 MB

class Solution:
    def maxAlternatingSum(self, A: List[int]) -> int:
        A = [abs(x) for x in A]
            
        A.sort()
        q = deque(A)

        s1 = 0
        s2 = 0
        while q:
            x = q.pop()
            s1 += x * x
            
            if q:
                x = q.popleft()
                s2 += x * x
        return s1 - s2
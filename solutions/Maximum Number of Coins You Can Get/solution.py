# Problem: Maximum Number of Coins You Can Get
# Language: python3
# Runtime: 644 ms
# Memory: 26.9 MB

class Solution:
    def maxCoins(self, A: List[int]) -> int:
        A.sort(reverse=True)
        A =deque(A)
        
        x,y,z=0,0,0
        while A:
            if len(A) >= 3:
                x += A.popleft()
                y += A.popleft()
                z += A.pop()
            elif len(A) == 2:
                x += A.popleft()
                y += A.popleft()
            else:
                return y
        return y
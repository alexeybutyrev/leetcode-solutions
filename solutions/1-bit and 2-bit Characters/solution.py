# Problem: 1-bit and 2-bit Characters
# Language: python3
# Runtime: 0 ms
# Memory: 17.7 MB

class Solution:
    def isOneBitCharacter(self, A: List[int]) -> bool:
        N = len(A)
        if N == 1:
            return A[0] == 0
        if N == 2:
            return A[0] == A[1] == 0
        A = deque(A)
        
        while A:
            x = A.popleft()
            if x == 0:
                if not A: return True
                continue
            y = A.popleft()
            if not A: return False
            
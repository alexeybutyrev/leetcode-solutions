# Problem: Reveal Cards In Increasing Order
# Language: python3
# Runtime: 32 ms
# Memory: 14.4 MB

class Solution:
    def deckRevealedIncreasing(self, A: List[int]) -> List[int]:
        A.sort()
        N = len(A)
        B = deque()
        while A:
            if B:
                b = B.pop()
                B.appendleft(b)
            
            a = A.pop()
            B.appendleft(a)
        
        return B
            
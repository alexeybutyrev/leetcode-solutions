# Problem: Fruits Into Baskets II
# Language: python3
# Runtime: 31 ms
# Memory: 17.8 MB

class Solution:
    def numOfUnplacedFruits(self, F: List[int], B: List[int]) -> int:
        seen = set()
        B = deque(B)
        ans = 0
        for f in F:
            mx = max(B)         
            if mx < f:
                ans += 1
            else:
                NB = deque()
                while B:
                    b = B.popleft()
                    if b >= f:
                        while B:
                            NB.append(B.popleft())
                    else:
                        NB.append(b)

                B = NB
                
        return ans
                
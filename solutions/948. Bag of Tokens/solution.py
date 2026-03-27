# Problem: Bag of Tokens
# Language: python3
# Runtime: 48 ms
# Memory: 14.3 MB

from collections import deque
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        tokens = deque(tokens)
        
        points = 0
        max_points = 0
        while tokens:
            if P >= tokens[0]:
                P -= tokens.popleft()
                points += 1
                max_points = max(max_points,points)
            else:
                if points > 0:
                    P += tokens.pop()
                    points -= 1
                else:
                    return max_points
        return max_points
        
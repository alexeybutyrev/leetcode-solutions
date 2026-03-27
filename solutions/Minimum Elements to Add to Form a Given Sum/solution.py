# Problem: Minimum Elements to Add to Form a Given Sum
# Language: python3
# Runtime: 744 ms
# Memory: 27.1 MB

class Solution:
    def minElements(self, A: List[int], limit: int, goal: int) -> int:
        N = len(A)
        S = sum(A)
        
        if S == goal:
            return 0
        
        if S < goal:
            k = (goal - S) // limit
            if k * limit + S >= goal:
                return k
            else:
                return k + 1
        else:
            k = (S - goal) // limit
            if -k * limit + S <= goal:
                return k
            else:
                return k + 1
        
        
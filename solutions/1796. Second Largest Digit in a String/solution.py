# Problem: Second Largest Digit in a String
# Language: python3
# Runtime: 44 ms
# Memory: 14.3 MB

class Solution:
    def secondHighest(self, s: str) -> int:
        A = set()
        for i,l in enumerate(s):
            if l.isdigit():
                A.add(int(l))
        if not A:
            return -1
        
        A = list(A)
        A.sort(reverse = True)
        
        return -1 if len(A) < 2 else A[1]
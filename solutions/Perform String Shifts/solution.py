# Problem: Perform String Shifts
# Language: python3
# Runtime: 32 ms
# Memory: 14.1 MB

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        def rotate_right(s,n):
            n = n % len(s)
            return s[-n:] + s[:-n]
        
        def rotate_left(s,n):
            n = n % len(s)
            return s[n:] + s[:n]

        final_shif = 0
        for sh in shift:
            if 0 == sh[0]:
                final_shif -= sh[1]
            else:
                final_shif += sh[1]
        
        return rotate_right(s, final_shif) if final_shif > 0 else rotate_left(s, -final_shif)

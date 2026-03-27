# Problem: Determine if Two Events Have Conflict
# Language: python3
# Runtime: 50 ms
# Memory: 13.9 MB

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def to_min(s):
            h,m = s.split(":")
            return int(h) * 60 + int(m)
        
        e1 = [to_min(event1[0]),to_min(event1[1])]
        e2 = [to_min(event2[0]),to_min(event2[1])]
        A = [e1,e2]
        A.sort()
        
        if A[-1][0] <= A[0][1]:
            return True
        return False
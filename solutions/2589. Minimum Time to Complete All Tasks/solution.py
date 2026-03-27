# Problem: Minimum Time to Complete All Tasks
# Language: python3
# Runtime: 890 ms
# Memory: 15.3 MB

class Solution:
    def findMinimumTime(self, A: List[List[int]]) -> int:
        A.sort(key=itemgetter(1))
        seen = set()
        for s, e, d in A:
            c = 0
            for x in range(s,e-d+1):
                if x in seen:
                    c += 1
            for x in range(e-d+1,e+1):
                if x not in seen:
                    if c:
                        c -= 1
                    else:
                        seen.add(x)
            
                    
        return len(seen)
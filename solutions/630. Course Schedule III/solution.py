# Problem: Course Schedule III
# Language: python3
# Runtime: 754 ms
# Memory: 19.9 MB

class Solution:
    def scheduleCourse(self, A: List[List[int]]) -> int:
        
        A.sort(key = lambda x: (x[1],x[0]))
        N = len(A)
        h = []
        start = 0
        for d, end in A:
            start += d
            heappush(h,-d)
            while start > end:
                start += heappop(h)
                
        return len(h)
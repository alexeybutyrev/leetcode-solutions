# Problem: Insert Interval
# Language: python3
# Runtime: 0 ms
# Memory: 19.5 MB

def merge(intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans = [ [intervals[0][0], intervals[0][1]] ]

        for a,b in intervals[1:]:
            if ans[-1][1] < a:
                ans.append([a,b])
            else:
                ans[-1][1] = max(ans[-1][1],b)
        return ans

class Solution:
    def insert(self, I: List[List[int]], NI: List[int]) -> List[List[int]]:
        
        return merge(I + [NI])
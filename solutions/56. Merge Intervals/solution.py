# Problem: Merge Intervals
# Language: python3
# Runtime: 7 ms
# Memory: 21.7 MB

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans = [ [intervals[0][0], intervals[0][1]] ]

        for a,b in intervals[1:]:
            if ans[-1][1] < a:
                ans.append([a,b])
            else:
                ans[-1][1] = max(ans[-1][1],b)
        return ans
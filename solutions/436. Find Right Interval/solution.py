# Problem: Find Right Interval
# Language: python3
# Runtime: 351 ms
# Memory: 20 MB

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        A = []
        
        for i,(s,e) in enumerate(intervals):
            A.append((s,i))
        
        A.sort()
        S = [s for s,i in A]
        ans = []
        N = len(A)
        for i,(s,e) in enumerate(intervals):
            ind = bisect_left(S,e)
            if ind == N and A[ind-1][0] < e:
                ans.append(-1)
                continue
            ans.append(A[ind][1])
        return ans
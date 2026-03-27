# Problem: Minimum Time Difference
# Language: python3
# Runtime: 78 ms
# Memory: 19.8 MB

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        A = []
        for t in timePoints:
            h,m = t.split(":")
            A.append(int(h)*60 +int(m))
            A.append((int(h)+24)*60 +int(m))
        
        ans = inf
        A.sort()
        for i in range(1,len(A)):
            ans = min(ans, A[i]-A[i-1])
        return ans
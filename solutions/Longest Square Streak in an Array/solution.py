# Problem: Longest Square Streak in an Array
# Language: python3
# Runtime: 104 ms
# Memory: 37.9 MB

class Solution:
    def longestSquareStreak(self, A: List[int]) -> int:
        A.sort()
        s = set(A)
        seen = set()
        ans = -1
        for x in A:
            if x not in seen:
                seen.add(x)
                lans = 1
                while x *x in s:
                    lans +=1
                    x*=x
                    seen.add(x)
                if lans >1:
                    ans = max(ans,lans)
        return ans
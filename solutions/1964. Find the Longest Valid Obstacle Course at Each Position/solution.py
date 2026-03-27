# Problem: Find the Longest Valid Obstacle Course at Each Position
# Language: python3
# Runtime: 1498 ms
# Memory: 34.6 MB

class Solution:
    def longestObstacleCourseAtEachPosition(self, A: List[int]) -> List[int]:
        
        ans = [1]
        B = [A[0]]

        for a in A[1:]:
            ind = bisect_right(B,a)
            if ind == len(B):
                B.append(a)
            else:
                B[ind] = a
            ans.append(ind+1)
        return ans
        
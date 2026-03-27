# Problem: Choose K Elements With Maximum Sum
# Language: python3
# Runtime: 351 ms
# Memory: 50.9 MB

class Solution:
    def findMaxSum(self, nums1: List[int], B: List[int], K: int) -> List[int]:
        Q = []
        I = [(x,i) for i,x in enumerate(nums1)]
        I.sort()
        ANS = [0] * len(nums1)
        s = 0
        b = 0
        for j,(x,i) in enumerate(I):
            if j and x > I[j-1][0]:
                ANS[i] = s
                b = s
            else:
                ANS[i] = b
            heappush(Q,B[i])
            s += B[i]
            if len(Q) > K:
                y = heappop(Q)
                s -= y
                
        return ANS
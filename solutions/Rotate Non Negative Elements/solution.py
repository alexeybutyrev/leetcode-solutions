# Problem: Rotate Non Negative Elements
# Language: python3
# Runtime: 141 ms
# Memory: 35.8 MB

class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        A = [x for x in nums if x >= 0]
        if not A: return nums
        def rotate(A, k):
            N = len(A)
            k %= N
            return A[k:] + A[:k]

        A = rotate(A,k)

        ANS = [0] * len(nums)
        j = 0
        for i,x in enumerate(nums):
            if x < 0:
                ANS[i] = x
            else:
                ANS[i] = A[j]
                j+=1
        return ANS
                
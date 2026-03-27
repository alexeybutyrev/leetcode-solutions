# Problem: Zero Array Transformation I
# Language: python3
# Runtime: 544 ms
# Memory: 59.7 MB

class Solution:
    def isZeroArray(self, nums: List[int], Q: List[List[int]]) -> bool:
        A  = []
        for a,b in Q:
            A.append((a,1))
            A.append((b+1,-1))
        A.sort()
        A = deque(A)
        N = len(nums)
        curr = 0
        I = []
        for i in range(N):
            if A and A[0][0] == i:
                while A and A[0][0] == i:
                    _, x = A.popleft()
                    curr += x
            I.append(curr)

        for x,y in zip(I, nums):
            if x < y:
                return False
        return True
            
# Problem: Lucky Numbers in a Matrix
# Language: python3
# Runtime: 115 ms
# Memory: 16.9 MB

class Solution:
    def luckyNumbers (self, A: List[List[int]]) -> List[int]:
        B = zip(*A)
        mx = []
        for x in B:
            mx.append(max(x))
        mn = []
        for x in A:
            mn.append(min(x))
        ans = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == mx[j] == mn[i]:
                    ans.append(A[i][j])
        return ans
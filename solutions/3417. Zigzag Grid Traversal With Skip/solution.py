# Problem: Zigzag Grid Traversal With Skip
# Language: python3
# Runtime: 0 ms
# Memory: 18 MB

class Solution:
    def zigzagTraversal(self, A: List[List[int]]) -> List[int]:
        pr = True
        ans = []
        for i in range(len(A)):
            if i%2 == 0:
                for j in range(len(A[0])):
                    if pr:
                        ans.append(A[i][j])
                    pr = not pr
            else:
                for j in range(len(A[0])-1,-1,-1):
                    if pr:
                        ans.append(A[i][j])
                    pr = not pr
        return ans
            
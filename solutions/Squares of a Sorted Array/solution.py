# Problem: Squares of a Sorted Array
# Language: python3
# Runtime: 159 ms
# Memory: 18.7 MB

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans = []
        N =len(A)
        i, j = 0, N - 1
        
        while i <=j:
            if abs(A[i]) > abs(A[j]):
                ans.append(A[i] * A[i])
                i += 1
            else:
                ans.append(A[j] * A[j])
                j -= 1
        return ans[::-1]
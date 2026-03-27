# Problem: Shuffle the Array
# Language: python3
# Runtime: 60 ms
# Memory: 19.5 MB

class Solution:
    def shuffle(self, A: List[int], n: int) -> List[int]:
        ans = []
        for x,y in zip(A[:n],A[n:2*n]):
            ans.append(x)
            ans.append(y)

        return ans
# Problem: Minimize Maximum Pair Sum in Array
# Language: python3
# Runtime: 859 ms
# Memory: 33.9 MB

class Solution:
    def minPairSum(self, A: List[int]) -> int:
        A.sort()
        A = deque(A)
        ans = 0 
        while A:
            ans = max(ans, A.popleft() + A.pop())
        return ans
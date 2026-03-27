# Problem: Sum of Mutated Array Closest to Target
# Language: python3
# Runtime: 138 ms
# Memory: 15.2 MB

class Solution:
    def findBestValue(self, A: List[int], target: int) -> int:
        
        A.sort(reverse=True)
        mx = max(A)
        while A and target >= A[-1] * len(A):
            target -= A.pop()
        return int(round((target - 0.0001) / len(A))) if A else mx
# Problem: Find the Maximum Sum of Node Values
# Language: python3
# Runtime: 935 ms
# Memory: 28.2 MB

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        best_sum = sum(max(n, k ^ n) for n in nums)
        cnt = sum((n ^ k) > n for n in nums)  
        return best_sum - (min(abs(n - (n ^ k)) for n in nums) if cnt % 2 else 0)
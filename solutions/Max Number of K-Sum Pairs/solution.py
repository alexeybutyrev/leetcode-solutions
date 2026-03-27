# Problem: Max Number of K-Sum Pairs
# Language: python3
# Runtime: 796 ms
# Memory: 27.4 MB

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        
        count = 0
        for n in nums:
            if (k != n << 1 and c[k - n] and c[n]) or (k == n << 1 and c[k-n] >=2):
                count += 1
                c[k-n] -= 1
                c[n] -=1
        return count
            
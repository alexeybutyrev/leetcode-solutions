# Problem: Subarray Sum Equals K
# Language: python3
# Runtime: 272 ms
# Memory: 16.4 MB

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = Counter()
        sm = 0
        c[0] = 1
        count = 0
        for n in nums:
            sm += n
            count += c[sm-k]
            c[sm] += 1
            
        return count
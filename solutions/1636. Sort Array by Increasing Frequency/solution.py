# Problem: Sort Array by Increasing Frequency
# Language: python3
# Runtime: 53 ms
# Memory: 16.7 MB

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        ans = []
        for v, x in sorted([(v,-k) for k,v in c.items()]):
            ans+= [-x]*v
        return ans
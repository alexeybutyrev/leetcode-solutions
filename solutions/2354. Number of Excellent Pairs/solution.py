# Problem: Number of Excellent Pairs
# Language: python3
# Runtime: 1186 ms
# Memory: 31.9 MB

class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        A = set(nums)
        c = Counter()
        for a in A:
            c[bin(a).count("1")] += 1
        
        ans = 0
        for a in range(0,32):
            for b in range(0,32):
                if a + b >= k:
                    ans += c[a] * c[b]
        
        return ans
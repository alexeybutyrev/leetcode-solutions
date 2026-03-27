# Problem: Count Special Triplets
# Language: python3
# Runtime: 819 ms
# Memory: 40.4 MB

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        
        L = Counter()
        R = Counter(nums)


        ans = 0
        for x in nums:
            R[x] -= 1
            ans += L[2*x] * R[2*x]
            ans %= (10**9 + 7)
            L[x] += 1

        return ans
# Problem: Find Nth Smallest Integer With K One Bits
# Language: python3
# Runtime: 3 ms
# Memory: 19.5 MB

class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        ans = 0

        for j in range(49, -1,-1):
            if k == 0:
                break

            c = comb(j,k)

            if n > c:
                n -= c
                ans |= (1 << j)
                k-=1
        return ans
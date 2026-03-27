# Problem: Count Subarrays With Majority Element I
# Language: python3
# Runtime: 7 ms
# Memory: 18 MB

class Solution:
    def countMajoritySubarrays(self, A: List[int], T: int) -> int:
        N = len(A)
        count = [1] + [0] * (N + N + 2)
        acc   = [1] + [0] * (N + N + 2)

        pre = ans = 0
        for x in A:
            pre += 1 if x == T else -1
            count[pre] += 1
            acc[pre] = acc[pre-1] + count[pre]
            ans += acc[pre-1]
        return ans
        
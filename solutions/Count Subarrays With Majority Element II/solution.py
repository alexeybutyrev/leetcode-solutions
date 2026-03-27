# Problem: Count Subarrays With Majority Element II
# Language: python3
# Runtime: 83 ms
# Memory: 32.2 MB

class Solution:
    def countMajoritySubarrays(self, A: List[int], T: int) -> int:
        N = len(A)
        count = [1] + [0] *( N + N + 2)
        acc = [1] + [0] * ( N + N + 2)

        ans = pre = 0
        for x in A:
            pre += 1 if x == T else -1
            count[pre] += 1
            acc[pre] = acc[pre-1] + count[pre]
            ans +=  acc[pre-1]
        return ans
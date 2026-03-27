# Problem: Count Subarrays With Cost Less Than or Equal to K
# Language: python3
# Runtime: 2103 ms
# Memory: 35.7 MB

from sortedcontainers import SortedList
class Solution:
    def countSubarrays(self, A: List[int], k: int) -> int:
        S = SortedList()
        ans = 0
        curr = 0
        for i,x in enumerate(A):
            S.add(x)
            
            while len(S) * (S[-1] - S[0]) > k:
                S.remove(A[curr])
                curr += 1
            ans += len(S)
        return ans
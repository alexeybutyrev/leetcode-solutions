# Problem: Count Number of Nice Subarrays
# Language: python3
# Runtime: 554 ms
# Memory: 23.3 MB

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        q = deque()
        c = 1
        ans=0
        for x in nums:
            if x & 1:
                if len(q)==k:
                    ans += q[0]*c
                    q.popleft()
                q.append(c)
                c = 1
            else:
                c+=1
        if len(q)==k:
            ans += q[0]*c
        return ans
            
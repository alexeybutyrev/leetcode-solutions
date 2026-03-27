# Problem: Rearrange Array Elements by Sign
# Language: python3
# Runtime: 1015 ms
# Memory: 47.9 MB

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = deque()
        neg = deque()
        
        for x in nums:
            if x > 0:
                pos.append(x)
            else:
                neg.append(x)
        
        ans = []
        while pos:
            ans.append(pos.popleft())
            ans.append(neg.popleft())
        return ans
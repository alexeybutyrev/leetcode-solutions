# Problem: Minimum Number of K Consecutive Bit Flips
# Language: python3
# Runtime: 833 ms
# Memory: 22.6 MB

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        stack = deque()
        ans=0
        for i,x in enumerate(nums):
            if x:
                if len(stack) & 1:
                    stack.append(i+k-1)
                    ans+=1
            else:
                if len(stack)&1 ==0:
                    stack.append(i+k-1)
                    ans+=1
            if stack and stack[0]==i:
                stack.popleft()
        return -1 if stack else ans
# Problem: Daily Temperatures
# Language: python3
# Runtime: 869 ms
# Memory: 30 MB

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)

        return ans
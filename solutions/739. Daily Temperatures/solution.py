# Problem: Daily Temperatures
# Language: python
# Runtime: 448 ms
# Memory: 16.3 MB

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        
        res = [0] * len(T)
        
        for i in range(len(T)-1,-1,-1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()

            if stack:
                res[i] = stack[-1]-i
            
            stack.append(i)
        
        return res
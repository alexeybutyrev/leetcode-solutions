# Problem: Diet Plan Performance
# Language: python3
# Runtime: 212 ms
# Memory: 22.6 MB

class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        n = len(calories)
        points = 0
        for i in range(n-k+1):
            if i > 0 and k > 1:
                s = s - calories[i-1] + calories[i+k-1]
            else:
                s = sum(calories[i:i+k])
                
            if s < lower:
                points -= 1
            if s > upper:
                points += 1
                
        return points
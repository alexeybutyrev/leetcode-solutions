# Problem: Average Salary Excluding the Minimum and Maximum Salary
# Language: python3
# Runtime: 28 ms
# Memory: 13.8 MB

class Solution:
    def average(self, salary: List[int]) -> float:
        min_, max_ = min(salary), max(salary)
        
        v = []
        for s in salary:
            if s not in [min_, max_]:
                v.append(s)
        
        return sum(v)/len(v)
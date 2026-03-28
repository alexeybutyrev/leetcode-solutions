# Problem: Find Numbers with Even Number of Digits
# Language: python3
# Runtime: 52 ms
# Memory: 14.3 MB

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        return sum([ len(str(n)) % 2 ==0 for n in nums ] )
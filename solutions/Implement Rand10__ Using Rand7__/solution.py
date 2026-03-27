# Problem: Implement Rand10() Using Rand7()
# Language: python3
# Runtime: 348 ms
# Memory: 16.5 MB

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        idx = 41
        while idx > 40:
            row = rand7() - 1
            col = rand7()
            idx = row * 7 + col
        return 1 + (idx-1) % 10 
        
        
        
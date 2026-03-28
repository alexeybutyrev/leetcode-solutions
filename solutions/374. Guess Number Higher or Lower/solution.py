# Problem: Guess Number Higher or Lower
# Language: python3
# Runtime: 28 ms
# Memory: 12.8 MB

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1,n
        
        while left <= right:
            
            pivot = left + (right - left) // 2
            print(left, right, pivot, guess(pivot))
            
            if guess(pivot) > 0:
                left = pivot+1
            elif guess(pivot) < 0:
                right = pivot-1
            else:
                return pivot
        
        return right
    
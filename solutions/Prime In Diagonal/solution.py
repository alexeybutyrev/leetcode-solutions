# Problem: Prime In Diagonal
# Language: python3
# Runtime: 830 ms
# Memory: 26.1 MB

def is_prime(num):
    """
    Check if a given number is a prime number.

    Args:
        num (int): The number to be checked.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False  # 0 and 1 are not prime numbers

    if num <= 3:
        return True  # 2 and 3 are prime numbers

    if num % 2 == 0 or num % 3 == 0:
        return False  # numbers divisible by 2 or 3 are not prime

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False  # numbers divisible by i or i + 2 are not prime
        i += 6

    return True  # if the number passes all the above checks, it is a prime number


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        ans = 0
        N = len(nums)
        for i in range(N):
            if is_prime(nums[i][i]):
                ans = max(ans, nums[i][i])
            if is_prime(nums[i][N - i - 1]):
                ans = max(ans, nums[i][N - i - 1])
        return ans
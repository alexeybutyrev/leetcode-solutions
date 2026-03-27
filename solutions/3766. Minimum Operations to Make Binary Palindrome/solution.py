# Problem: Minimum Operations to Make Binary Palindrome
# Language: python3
# Runtime: 668 ms
# Memory: 18.5 MB

class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        def is_pali(x):
            s = bin(x)[2:]
            return s == s[::-1]

        ans = []
        for x in nums:
            
            for j in range(5000):
                if is_pali(x + j):
                    ans.append(j)
                    break
                if is_pali(x - j):
                    ans.append(j)
                    break
                
        return ans
            
            
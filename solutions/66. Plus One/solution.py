# Problem: Plus One
# Language: python
# Runtime: 16 ms
# Memory: 11.8 MB

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in reversed(range(len(digits))):
            print(i)
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        return  [1] + digits
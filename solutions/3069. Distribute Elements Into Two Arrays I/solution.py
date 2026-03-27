# Problem: Distribute Elements Into Two Arrays I
# Language: python3
# Runtime: 40 ms
# Memory: 16.6 MB

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        A1 = [nums.pop(0)]
        A2 = [nums.pop(0)]
        
        while nums:
            x = nums.pop(0)
            if A1[-1] > A2[-1]:
                A1.append(x)
            else:
                A2.append(x)
        return A1 + A2
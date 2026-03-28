# Problem: Check If All 1's Are at Least Length K Places Away
# Language: python3
# Runtime: 1196 ms
# Memory: 16.5 MB

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:

        n  = len(nums)
        
        
        ind = 0
        if nums[ind] != 1:
            for i in range(n):
                if nums[i] == 1:
                    ind = i
                    break
        
            if ind == 0:
                return True
        
        count = 0
        for i in range(ind+1, n):
            if nums[i] == 1:
                if count < k and ind != n-1:
                    return False
                else:
                    count = 0
            else:
                 count += 1
        
        return True
    
            
            
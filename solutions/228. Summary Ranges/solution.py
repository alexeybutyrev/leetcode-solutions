# Problem: Summary Ranges
# Language: python3
# Runtime: 32 ms
# Memory: 14 MB

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        res = []
        start = str(nums[0])
        end = None
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                end = str(nums[i])
            else:
                if end is not None:
                    res.append(start + "->" + end)
                else:
                    res.append(start)
                end = None
                start = str(nums[i])
                
        if end is not None:
            res.append(start + "->" + end)
        else:
            res.append(start)
        
        
        return res
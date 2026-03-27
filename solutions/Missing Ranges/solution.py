# Problem: Missing Ranges
# Language: python3
# Runtime: 28 ms
# Memory: 14.3 MB

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums:
            if lower!=upper:
                return [str(lower) + "->" + str(upper)]
            else:
                return [str(lower)]
        N = len(nums)
        s = ""
        k = 0
        n = lower
        ans = []
        
        for i in range(N):
            if nums[i] == n:
                n += 1
            else:
                s = str(n)
                if nums[i] - 1 != n:
                    if i == 0:
                        s = str(lower) + "->" + str(nums[i]-1)
                    else:
                        s += "->" + str(nums[i]-1)
                
                ans.append(s)
                n = nums[i]+1
        
        if nums[N-1] != upper:
            s = str(n)
            if n != upper:
                s += "->" + str(upper)
                
            ans.append(s)
        
        return ans
                    
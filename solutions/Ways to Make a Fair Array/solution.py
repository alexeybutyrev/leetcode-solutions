# Problem: Ways to Make a Fair Array
# Language: python3
# Runtime: 2288 ms
# Memory: 21.1 MB

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        
        
        
        n = len(nums)
        so = [0] * n
        se = [0] * n

        so[0] = nums[0]
        o = nums[0] 
        e = 0
        
        for i in range(1,n):
            so[i] = so[i-1]
            se[i] = se[i-1]
            if i % 2 == 0:
                o += nums[i]
                so[i] += nums[i]
            else:
                e += nums[i]
                se[i] += nums[i]

        #print(so,se)
        
        count = 0
        for i in range(n):
            if i %2 != 0 :
                s1 = so[i] + (e - se[i])
                s2 = se[i] + (o - so[i]) - nums[i]
            else:
                s1 = so[i] + (e - se[i]) - nums[i]
                s2 = se[i] + (o - so[i])
            
            count += int(s1 == s2)
        return count
# Problem: Sort the Jumbled Numbers
# Language: python3
# Runtime: 1160 ms
# Memory: 24.7 MB

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        A = []
        for i,x in enumerate(nums):
            s = ''
            for d in str(x):
                s += str(mapping[int(d)])
            
            s = s.lstrip("0")
            
            A.append((int(s) if s else 0,i))
        
        A.sort()

        return [nums[i] for _,i in A]
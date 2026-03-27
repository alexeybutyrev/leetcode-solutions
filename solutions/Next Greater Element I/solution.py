# Problem: Next Greater Element I
# Language: python3
# Runtime: 75 ms
# Memory: 14.5 MB

class Solution:
    def nextGreaterElement(self, nums1: List[int], A: List[int]) -> List[int]:
        
        hm = {}
        
        stack = []
        for x in A:
            while stack and stack[-1] < x:
                hm[stack.pop()] = x
            stack.append(x)

        return [-1 if a not in hm else hm[a] for a in nums1]
                    
        
# Problem: How Many Apples Can You Put into the Basket
# Language: python3
# Runtime: 44 ms
# Memory: 14.3 MB

class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        s = 0
        i = 0
        while i < len(arr) and s <= 5000:
            s += arr[i]
            i+=1
        
        return i - 1 if s > 5000 else i
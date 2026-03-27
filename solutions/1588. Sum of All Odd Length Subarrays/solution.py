# Problem: Sum of All Odd Length Subarrays
# Language: python3
# Runtime: 80 ms
# Memory: 14 MB

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        s = 0
        for i in range(n):
            for l in range(n):
                if l %2 != 0 and i+l <= n:
                    #print(arr[i:i+l])
                    s+=sum(arr[i:i+l])
        if n % 2 != 0:
            s+=sum(arr)
        return s
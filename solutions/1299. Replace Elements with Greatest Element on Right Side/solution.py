# Problem: Replace Elements with Greatest Element on Right Side
# Language: python3
# Runtime: 6008 ms
# Memory: 15 MB

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n-1):
            arr[i] = max(arr[i+1:])
        arr[n-1] = -1
        return arr
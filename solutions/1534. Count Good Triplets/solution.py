# Problem: Count Good Triplets
# Language: python3
# Runtime: 700 ms
# Memory: 14.4 MB

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        N = len(arr)
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j + 1, N):
                    if (abs(arr[i] - arr[j]) <= a and 
                        abs(arr[j] - arr[k]) <= b and 
                        abs(arr[i] - arr[k]) <= c 
                       ):
                        count += 1
        return count
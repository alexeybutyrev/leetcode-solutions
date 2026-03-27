# Problem: Least Number of Unique Integers after K Removals
# Language: python3
# Runtime: 323 ms
# Memory: 33.3 MB

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        
        A = list(c.values())
        A.sort(reverse=True)
        while A:
            x = A.pop()
            if x <= k:
                k-=x
            else:
                return len(A)+1
        return 0
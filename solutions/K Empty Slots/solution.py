# Problem: K Empty Slots
# Language: python3
# Runtime: 1388 ms
# Memory: 17.3 MB

from sortedcontainers import SortedList
class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:

        A = SortedList()
        k+=1
        for i,b in enumerate(bulbs):
            ind = A.bisect(b)
            if(ind > 0 and b - A[ind - 1] == k) or (ind < len(A) and A[ind] - b == k):
                return i + 1
            A.add(b)
            
        return -1
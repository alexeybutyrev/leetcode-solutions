# Problem: Last Stone Weight
# Language: python3
# Runtime: 24 ms
# Memory: 13.6 MB

"""
import heapq
listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
heapq.heapify(listForTree)             # for a min heap
heapq._heapify_max(listForTree)        # for a maxheap!!
If you then want to pop elements, use:

heapq.heappop(minheap)      # pop from minheap
heapq._heappop_max(maxheap) # pop from maxheap

"""


import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)
        print(list(stones))
        
        while len(stones) > 1:
            m1 = heapq.heappop(stones)
            m2 = heapq.heappop(stones)
            
            if m1 != m2:
                heapq.heappush(stones,m1-m2)
            
            print(list(stones))
        
        return -heapq._heappop_max(stones) if len(stones) == 1 else 0
            
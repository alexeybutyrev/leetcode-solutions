# Problem: Minimum Time to Build Blocks
# Language: python3
# Runtime: 62 ms
# Memory: 16.5 MB


class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        
        heapq.heapify(blocks)
        while len(blocks) > 1:
            x, y = heapq.heappop(blocks), heapq.heappop(blocks)
            heapq.heappush(blocks, y + split)
        return heapq.heappop(blocks)
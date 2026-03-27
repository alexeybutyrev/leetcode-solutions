# Problem: Most Visited Sector in  a Circular Track
# Language: python3
# Runtime: 48 ms
# Memory: 14 MB

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        end = rounds[-1]
        start = rounds[0]
        if start <= end:
            return list(range(start, end+1))
        
        return list(range(1,end+1)) + list(range(start,n+1))
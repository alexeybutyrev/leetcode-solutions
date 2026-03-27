# Problem: Unique Number of Occurrences
# Language: python3
# Runtime: 43 ms
# Memory: 17.4 MB

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        return len(set(Counter(arr).values()))==len(set(arr))
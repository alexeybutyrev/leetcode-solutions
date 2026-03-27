# Problem: Queue Reconstruction by Height
# Language: python3
# Runtime: 84 ms
# Memory: 14.9 MB

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        
        ans = []
        
        for p in people:
            ans.insert(p[1], p)
        
        return ans
        
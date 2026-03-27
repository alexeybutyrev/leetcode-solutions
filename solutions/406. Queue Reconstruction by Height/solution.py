# Problem: Queue Reconstruction by Height
# Language: python3
# Runtime: 193 ms
# Memory: 14.7 MB

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        hp = []
        for h,n in people:
            heappush(hp, (-h,n))
        
        ans = []
        while hp:
            h,n = heappop(hp)
            h = -h
            if ans:
                ans.insert(n,(h,n))
            else:
                ans.append((h,n))
        return ans
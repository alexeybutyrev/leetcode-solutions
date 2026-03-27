# Problem: Queries on Number of Points Inside a Circle
# Language: python3
# Runtime: 828 ms
# Memory: 14.7 MB

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for x,y,r in queries:
            count = 0
            for xc, yc in points:
                if (x - xc) * (x - xc) + (y - yc) * (y - yc) <= r * r:
                    count += 1
            ans.append(count)
        return ans
        
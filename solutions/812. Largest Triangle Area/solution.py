# Problem: Largest Triangle Area
# Language: python3
# Runtime: 91 ms
# Memory: 19.6 MB

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        N = len(points)
        poins = list(set((x,y) for x,y in points))
        h = []
        ans = 0
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1,N):
                    try:
                        x1,y1 = points[i]
                        x2,y2 = points[j]
                        x3,y3 = points[k]
                        a = sqrt((x1-x2)*(x1-x2) + (y1-y2) * (y1-y2))
                        b = sqrt((x1-x3)*(x1-x3) + (y1-y3) * (y1-y3))
                        c = sqrt((x3-x2)*(x3-x2) + (y3-y2) * (y3-y2))
                        p = 0.5 * (a + b + c)
                        ans = max(ans, sqrt(p*(p-c)*(p-b)*(p-a)))
                    except:
                        print(points[i],points[j],points[k])
                        print(p,a,b,c)
                    
        
        return  ans
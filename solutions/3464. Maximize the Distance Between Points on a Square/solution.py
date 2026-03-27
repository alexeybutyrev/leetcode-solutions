# Problem: Maximize the Distance Between Points on a Square
# Language: python3
# Runtime: 667 ms
# Memory: 23.9 MB

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], K: int) -> int:
        
        dist = lambda x,y: abs(x[0] - y[0]) + abs(x[1] - y[1])
        
        pts = [[], [], [], []] # Left, Top, Right, Bottom
        for x, y in points:
            if x == 0 and y != 0: pts[0].append((x,y))
            elif x != 0 and y == side: pts[1].append((x,y))
            elif x == side and y != side: pts[2].append((x,y))
            else: pts[3].append((x,y))
        
        # Sort points in each line (Right and Bottom lines are
        # sorted in reverse to sort all points in clockwise dir)
        pts[0].sort()
        pts[1].sort()
        pts[2].sort(reverse=True)
        pts[3].sort(reverse=True)
        G = [*pts[0],*pts[1],*pts[2],*pts[3]] # Recombine points
        
        

        NG = len(G)
        def check(d):
            D = deque([(0,0,1)])
            ret = 1

            for i in range(1,NG):
                mln = 1
                i2 = i
                while D:
                    j, k, ln = D[0]
                    if dist(G[i], G[j]) >= d:
                        if ln + 1 >= mln and dist(G[i], G[k]) >= d:
                            i2 = k
                            mln = ln + 1
                            ret = max(ret, mln)
                        D.popleft()
                    else:
                        break
                D.append((i,i2,mln))


            return ret >= K
        lo, hi = 0, side

        while lo <= hi:
            mid = lo + hi >> 1

            if check(mid):
                lo = mid + 1
            else:
                hi = mid - 1
                
                
        return hi

        
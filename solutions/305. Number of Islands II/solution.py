# Problem: Number of Islands II
# Language: python3
# Runtime: 834 ms
# Memory: 21.5 MB

class Solution:
    def numIslands2(self, N: int, M: int, positions: List[List[int]]) -> List[int]:
        UF = {}
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
    
        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)
        
        A = [[0] * M for _ in range(N)]
        seen = set()
        ans = []
        parents = set()
        curr = 0
        for i,j in positions:
            if A[i][j] == 0:
                union((i,j),(i,j))
                seen.add((i,j))
                A[i][j] = 1
                curr += 1
                # before
                s = set()
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0),(0,0)]:
                    x = i + dx
                    y = j + dy
                    if  N > x >= 0 and M > y >= 0 and A[x][y]:
                        s.add(find((x,y)))
                nb = len(s)

                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    x = i + dx
                    y = j + dy
                    if  N > x >= 0 and M > y >= 0 and A[x][y]:
                        union((i,j),(x,y))

                s = set()
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0),(0,0)]:
                    x = i + dx
                    y = j + dy
                    if  N > x >= 0 and M > y >= 0 and A[x][y]:
                        s.add(find((x,y)))
                na = len(s)
                curr -= nb - na
            
            ans.append(curr)
        
        return ans
                       
                
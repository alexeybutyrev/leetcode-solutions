# Problem: Prison Cells After N Days
# Language: python3
# Runtime: 56 ms
# Memory: 14 MB

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        #cells = [0, 0, 0, 0]
        n = len(cells)
        def run(N, cells):
            dp = []
            mat = []
            found = False
            for l in range(N):
                key = "".join(map(str,cells))
                if key not in dp:
                    new_cells = cells[:]
                    for i in range(n):
                        if i > 0 and i < n-1 and cells[i-1] == cells[i+1]:
                            new_cells[i] = 1
                        else:
                            new_cells[i] = 0
                    
                    cells = new_cells[:]
                    mat.append(cells)
                    dp.append(key)
                else:
                    
                    found = True
                    break
            
            if not found:
                return cells
            
            key_index = dp.index(key)
            mat = mat[key_index:]
            N = N - l
            
            ind = (N - 1) % len(mat) 
            
            return mat[ind]
        
        return run(N, cells)
        
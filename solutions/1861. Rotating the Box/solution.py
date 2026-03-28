# Problem: Rotating the Box
# Language: python3
# Runtime: 5104 ms
# Memory: 23.8 MB

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        M = len(box[0])
        for r in box:
            
            for i in range(M-2,-1,-1):
                if r[i] == "#" and r[i+1] == ".":
                    j = i
                    while j < M-1 and r[j] == "#" and r[j+1] == ".":
                        r[j], r[j+1] = r[j+1], r[j]
                        j += 1
        
        return map(reversed,zip(*box))
                
        
                
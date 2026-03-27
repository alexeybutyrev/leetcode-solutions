# Problem: Find the Largest Area of Square Inside Two Rectangles
# Language: python3
# Runtime: 3571 ms
# Memory: 20.1 MB

def overlap_area(square1, square2):
    # Extracting coordinates of squares
    x1, y1, x2, y2 = square1
    a1, b1, a2, b2 = square2
    
    # Calculating overlap coordinates
    overlap_x1 = max(x1, a1)
    overlap_y1 = max(y1, b1)
    overlap_x2 = min(x2, a2)
    overlap_y2 = min(y2, b2)
    
    # Calculating overlap area
    overlap_width = max(0, overlap_x2 - overlap_x1)
    overlap_height = max(0, overlap_y2 - overlap_y1)
    overlap_area = overlap_width * overlap_height
    x = min(overlap_width, overlap_height)
    return x * x

class Solution:
    def largestSquareArea(self, BL: List[List[int]], TR: List[List[int]]) -> int:
        N = len(BL)
        A = []
        for i in range(N):
            A.append([BL[i][0], BL[i][1], TR[i][0], TR[i][1]])
        A.sort()
        
        ans = 0
        for i in range(N):
            for j in range(i+1, N):    
                ans = max(ans,overlap_area(A[i],A[j]))
                
        return ans
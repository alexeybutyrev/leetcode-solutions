# Problem: Number of Ships in a Rectangle
# Language: python3
# Runtime: 46 ms
# Memory: 16.5 MB

# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', TR: 'Point', BL: 'Point') -> int:
        if BL.x > TR.x or BL.y > TR.y: return 0
        if not sea.hasShips(TR,BL): return 0
        if BL.x == TR.x and BL.y == TR.y: return 1
        
        mx = (BL.x + TR.x) // 2
        my = (BL.y + TR.y) // 2
        
        return self.countShips(sea, Point(mx, TR.y), Point(BL.x, my + 1)) + \
               self.countShips(sea, Point(mx, my), BL) + \
               self.countShips(sea, Point(TR.x, my), Point(mx+1, BL.y)) + \
               self.countShips(sea, TR, Point(mx+1, my+1))
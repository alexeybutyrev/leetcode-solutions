# Problem: Video Stitching
# Language: python3
# Runtime: 36 ms
# Memory: 14.1 MB

from heapq import *
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        
        lm, rm = -1, 0
        count = 0 
        print(sorted(clips))
        for l,r in sorted(clips):
            if l > rm or rm >=T:
                break
            elif lm < l <= rm:
                count += 1
                lm = rm
                
            rm = max(rm, r)
        
        return count if rm >= T else -1
    
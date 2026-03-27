# Problem: Flipping an Image
# Language: python3
# Runtime: 48 ms
# Memory: 14.1 MB

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for a in A:
            a.reverse()
        
        for a in A:
            for i in range(len(a)):
                a[i] ^= 1
        return A
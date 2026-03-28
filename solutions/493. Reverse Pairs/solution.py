# Problem: Reverse Pairs
# Language: python3
# Runtime: 1288 ms
# Memory: 21.9 MB

class Node:
    def __init__(self, val):
        self.val   = val
        self.get_cnt = 0
        self.left  = None
        self.right = None
    
    def add(self, x):
        
        if x < self.val:
            if not self.left:
                self.left = Node(x)
            else:
                self.left.add(x)
        else:
            self.get_cnt += 1
            if not self.right:
                self.right = Node(x)
            else:
                self.right.add(x)
    
    def search(self, x):
        if self.val > x:
            sr = self.right.search(x) if self.right else 0            
            return  sr + self.get_cnt
        elif self.val == x:
            return self.get_cnt
        else:
            return self.right.search(x) if self.right else 0

class Solution:
    def reversePairs(self, A: List[int]) -> int:
        
        def mergesort(A):
            if len(A) <= 1:
                return A, 0
            
            m = len(A) // 2
            
            L, cl = mergesort(A[:m])
            R, cr = mergesort(A[m:])
            
            count = cl + cr
            
            for r in R:
                c = len(L) - bisect.bisect_right(L, 2 * r)
                
                if c == 0:
                    break
                count += c
            
            return sorted(L+R), count
        
        return mergesort(A)[1]
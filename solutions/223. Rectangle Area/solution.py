# Problem: Rectangle Area
# Language: python3
# Runtime: 3 ms
# Memory: 19.8 MB

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        Sa = (ax2-ax1) * (ay2 - ay1)
        Sb = (bx2-bx1) * (by2 - by1)
        if Sa == 0: return Sb
        if Sb == 0: return Sa

        if  (bx2 <= ax2 and 
             bx1 >= ax1 and
             by2 <= ay2 and 
             by1 >= ay1
            ):
            return Sa
        
        if  (ax2 <= bx2 and 
             ax1 >= bx1 and
             ay2 <= by2 and 
             ay1 >= by1
            ):
            return Sb
        

        X = [[ax1,ax2], [bx1,bx2]]
        X.sort()
        if X[0][1] >= X[1][0]:
            x1 = max(X[0][0], X[1][0])
            x2 = min(X[0][1], X[1][1])
            x = x2 - x1
        else:
            x = 0

        Y = [[ay1,ay2], [by1,by2]]
        Y.sort()
        if Y[0][1] >= Y[1][0]:
            y1 = max(Y[0][0], Y[1][0])
            y2 = min(Y[0][1], Y[1][1])
            y = y2 - y1
        else:
            y = 0
        
        
        print(Sa,Sb,x,y)
        return Sa + Sb - x * y
        
# Problem: Distribute Elements Into Two Arrays II
# Language: python3
# Runtime: 1590 ms
# Memory: 36.8 MB

from sortedcontainers import SortedList
class Solution:
    def resultArray(self, A: List[int]) -> List[int]:
        ans = []
        L = []
        R = []
        sL = SortedList()
        sR = SortedList()
        for i,x in enumerate(A):
            if i == 0:
                L.append(i)
                sL.add(x)
            elif i == 1:
                R.append(i)
                sR.add(x)
            else:
                n1 = len(L)
                n2 = len(R)
                c1 = n1 - sL.bisect_right(x)
                c2 = n2 - sR.bisect_right(x)
                print(c1,c2)
                if c1 > c2:
                    L.append(i)
                    sL.add(x)
                elif c1 < c2:
                    R.append(i)
                    sR.add(x)
                else:
                    if n2 < n1:
                        R.append(i)
                        sR.add(x)
                    else:
                        L.append(i)
                        sL.add(x)
                        
        
        for x in L:
            ans.append(A[x])
        for x in R:
            ans.append(A[x])
        
        return ans
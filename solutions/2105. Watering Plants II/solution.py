# Problem: Watering Plants II
# Language: python3
# Runtime: 1058 ms
# Memory: 26.5 MB

class Solution:
    def minimumRefill(self, P: List[int], A: int, B: int) -> int:

        i,j = 0, (N := len(P)) - 1
        a,b = A,B
        ans = 0
        while i < j:
            if P[i] <= a:
                a -= P[i]
                P[i] = 0
                i+=1
            else:
                ans += 1
                a = A
                if P[i] <= a:
                    a -= P[i]
                    P[i] = 0
                    i += 1
                else:
                    P[i]-=a
            
            
            if P[j] <= b:
                b -= P[j]
                P[j] = 0
                j -=1
            else:
                ans += 1
                b = B
                if P[j] <= b:
                    b -= P[j]
                    P[j] = 0
                    j -= 1
                else:
                    P[j]-=b

        if P[i] > 0:
            if P[i] <= max(a,b):
                return ans
            else:
                while P[i] > 0:
                    a = A
                    ans += 1
                    P[i] -= a
                    if P[i] <= 0:
                        return ans
                    
                    b = B
                    ans += 1
                    P[i] -= b
                    if P[i] <= 0:
                        return ans
                    
        return ans
            
                
        
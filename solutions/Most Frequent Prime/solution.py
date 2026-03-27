# Problem: Most Frequent Prime
# Language: python3
# Runtime: 91 ms
# Memory: 16.7 MB

def is_prime(num):
    """
    Check if a number is prime.
    
    Args:
    num (int): The number to be checked.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        c = Counter()
        A = []
        for x in mat:
            la = []
            for a in x:
                la.append(str(a))
            A.append(la)
            
        N = len(A)
        M = len(A[0])
        
        d = [(0,1),(0,-1),
             (-1,0),(1,-1),
             (1,1),(-1,-1),
             (1,0),(-1,1),]
        
        def walk(i,j):
            for dx,dy in d:
                curr = A[i][j]
                x = i + dx
                y = j + dy
                while 0 <= x < N and 0 <= y < M:
                    
                    curr += A[x][y]
                    c[curr] += 1
                    x += dx
                    y += dy
                    
        
        
        ans = -1
        
        for i in range(N):
            for j in range(M):
                walk(i, j)
        count = 0
        #print(c)
        for x,v in c.items():
            y = int(x)
            if v >= count and is_prime(int(y)):
                if v == count:
                    ans = max(ans, y)
                else:
                    ans = y
                count = v
        return ans
        
        
        
            
        
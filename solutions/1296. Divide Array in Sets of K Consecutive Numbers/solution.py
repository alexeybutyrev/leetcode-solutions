# Problem: Divide Array in Sets of K Consecutive Numbers
# Language: python3
# Runtime: 444 ms
# Memory: 35.2 MB

class Solution:
    def isPossibleDivide(self, nums: List[int], K: int) -> bool:
        c = Counter(nums)
        
        A = [(k,v) for k,v in c.items()]
        A.sort(reverse = True)
        
        
        while A:
            if len(A) < K:
                return False
            B = deque()
            for i in range(K-1):
                d, val = A.pop()
                if d != A[-1][0] - 1:
                    return False
                val -= 1
                if val:
                    B.appendleft((d,val))
            
            d, val = A.pop()
            val -= 1
            if val:
                B.appendleft((d,val))

            for d,v in B:
                A.append((d,v))
                
            
        return True
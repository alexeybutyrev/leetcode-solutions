# Problem: Sum of Numbers With Units Digit K
# Language: python3
# Runtime: 692 ms
# Memory: 14.2 MB

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        hm = set()
        k = str(k)
        ans = 0
        st = set()
        for i in range(num+1):
            if k == str(i)[-1]:
                hm.add(i)
        
        
        q = deque([0])
        seen = {0}
        count = 0
        while q:
            L = len(q)
            for _ in range(L):
                x = q.popleft()
                if x == num:
                    return count
                
                for n in hm:
                    if x + n <= num and x + n not in seen:
                        seen.add(x+n)
                        q.append((x+n))
            
            count += 1
        return -1
            
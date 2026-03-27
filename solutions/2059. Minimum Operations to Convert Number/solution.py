# Problem: Minimum Operations to Convert Number
# Language: python3
# Runtime: 4108 ms
# Memory: 183.9 MB

class Solution:
    def minimumOperations(self, A: List[int], start: int, goal: int) -> int:
        q = deque([start])
        seen = {start}
        
        count = 0
        while q:
            
            L = len(q)
            for _ in range(L):
                num = q.popleft()
                if num == goal:
                    return count
                if num > 1000 or num < 0:
                    continue
                for a in A:
                    x = num - a
                    if x not in seen:
                        seen.add(x)
                        q.append(x)
                    x = num + a
                    if x not in seen:
                        seen.add(x)
                        q.append(x)
                    x = num ^ a
                    if x not in seen:
                        seen.add(x)
                        q.append(x)

            count += 1
                
        
        return -1
            
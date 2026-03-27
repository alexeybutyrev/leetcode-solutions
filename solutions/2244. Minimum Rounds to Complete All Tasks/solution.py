# Problem: Minimum Rounds to Complete All Tasks
# Language: python3
# Runtime: 1183 ms
# Memory: 28 MB

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = Counter(tasks)
        ans = 0
        for a in c.values():
            if a == 1:
                return -1
            
            c = a // 2
            x = inf
            for i in range(c+1):
                if (a - i * 2) % 3 == 0:
                    x = min(x,i + (a - i * 2) // 3)
            
            c = a // 3
            for i in range(c+1):
                if (a - i * 3) % 2 == 0:
                    x = min(x,i + (a - i * 3) // 2)
            
            ans += x
            
        return ans
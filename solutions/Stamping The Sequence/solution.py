# Problem: Stamping The Sequence
# Language: python3
# Runtime: 272 ms
# Memory: 14.5 MB

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        masks = [(1 << m) - 1] * (n - m + 1)
        target_mask = (1 << n) - 1
        
        q = deque()
        visited = set()
        for i in range(n-m+1):
            for j in range(m):
                masks[i] ^= (1 << j) * (target[j+i] == stamp[j])
                
                if not masks[i]:
                    q.append(i)
                    visited.add(i)
                    
        ans = []
        while q and target_mask != 0:
            cand = q.popleft()
            ans.append(cand)
            to_update = [i for i in range(cand, min(n, cand + m)) if target_mask & (1<<i)]

            for i in to_update:
                for j in range(max(0, i - m + 1), min(i + 1, n - m + 1)):
                    masks[j] = masks[j] - (masks[j] & (1<<(i - j)))
                target_mask ^= (1<<i)

            for j in range(max(0, cand - m + 1), min(cand + m, n - m + 1)):
                if masks[j] == 0 and j not in visited:
                    visited.add(j)
                    q.append(j)
        
        return ans[::-1] if target_mask == 0 else []
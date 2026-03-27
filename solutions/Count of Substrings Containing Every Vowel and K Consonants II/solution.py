# Problem: Count of Substrings Containing Every Vowel and K Consonants II
# Language: python3
# Runtime: 2524 ms
# Memory: 19 MB

class Solution:
    def countOfSubstrings(self, S: str, k: int) -> int:
        N = len(S)
        ans = 0
        count = 0
        l = 0
        c = Counter()
        CONST = 0
        fill_ind = -1
        Q = deque()
        s = 0
        for r in range(N):
            x = S[r]
            c[x] += 1
            Q.append(x)
            if x not in ['a', 'e', 'i', 'o', 'u']:
                CONST += 1
            
            if CONST > k:
                s = 0
                while CONST > k:
                    curr = S[l]

                    c[curr] -= 1
                    if not c[curr]:
                        del c[curr]
                    
                    if curr not in ['a', 'e', 'i', 'o', 'u']:
                        CONST -= 1
                    Q.popleft()
                    l+=1
            
            if CONST == k:
                for a in ['a', 'e', 'i', 'o', 'u']:
                    if not c[a]:
                        break
                else:

                    while Q and Q[0] in ['a', 'e', 'i', 'o', 'u'] and c[Q[0]] and c[Q[0]] > 1:
                        s += 1
                        l+=1
                        c[Q[0]] -= 1
                        Q.popleft()
                        
                    ans += s + 1
        return ans
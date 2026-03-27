# Problem: Push Dominoes
# Language: python3
# Runtime: 291 ms
# Memory: 17.9 MB

class Solution:
    def pushDominoes(self, D: str) -> str:
        b = 0
        R = []
        for a in D:
            if a == "R":
                b = 1
                R.append(1)
            elif a == "L":
                R.append(0)
                b = 0
            else:
                R.append(b)
        
        b = 0
        L = []
        for a in D[::-1]:
            if a == "L":
                b = 1
                L.append(1)
            elif a == "R":
                L.append(0)
                b = 0
            else:
                L.append(b)
        L = L[::-1]

        ans = ""
        c = 0
        for r,l in zip(R,L):
            if r == 1 and l == 0:
                if c > 0:
                    ans += (c // 2) * 'R' + '.' * (c % 2 != 0) + (c // 2) * 'L'
                    
                ans += "R"
                c = 0
            elif r == 0 and l == 1:
                if c > 0:
                    ans += (c // 2) * 'R' + '.' * (c % 2 != 0) + (c // 2) * 'L'
                ans += "L"
                c = 0
            elif l == 0 and r == 0:
                ans += '.'
            else:
                c += 1
        if c > 0:
            ans += (c // 2) * 'R' + '.' * (c % 2 != 0) + (c // 2) * 'L'
        return ans
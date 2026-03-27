# Problem: Reconstruct Original Digits from English
# Language: python3
# Runtime: 40 ms
# Memory: 14.9 MB

class Solution:
    def originalDigits(self, s: str) -> str:
        digits = ["zero","one","two", "three", "four", "five", "six", "seven", "eight", "nine"]
        digits = ["","","", "", "", "", "", "", "", "nine"]
        dc = map(Counter, digits)
        
        c = Counter(s)
        ans = ''
        if 'z' in c:
            v = c['z']
            ans += '0' * v
            del c['z']
            for l in ['o','r','e']:
                if c[l] == v:
                    del c[l]
                else:
                    c[l] -= v

        if 'x' in c:
            v = c['x']
            ans += '6' * v
            del c['x']
            for l in ['s','i']:
                if c[l] == v:
                    del c[l]
                else:
                    c[l] -= v
        

        if 'w' in c:
            v = c['w']
            ans += '2' * v
            del c['w']
            for l in ['t','o']:
                if c[l] == v:
                    del c[l]
                else:
                    c[l] -= v

        if 'u' in c:
            v = c['u']
            ans += '4' * v
            del c['u']
            for l in ['f','o','r']:
                if c[l] == v:
                    del c[l]
                else:
                    c[l] -= v

        if 'o' in c:
            v = c['o']
            ans += '1' * v
            del c['o']
            for l in ['n','e']:
                if c[l] == v:
                    del c[l]
                else:
                    c[l] -= v
                
        if 'f' in c:
            v = c['f']
            ans += '5' * v
            del c['f']
            for l in ['i','v','e']:
                if c[l] == v:
                    del c[l]
                else:
                    c[l] -= v
                
        if 'v' in c:
            v = c['v']
            ans += '7' * v
            del c['v']
            for l in ['s','n']:
                if c[l] == v:
                    del c[l]
                else:
                    c[l] -= v
            
            if c['e'] == 2*v:
                del c['e']
            else:
                c['e'] -= 2*v
        
        if 'g' in c:
            v = c['g']
            ans += '8' * v
            del c['g']
            for l in ['e','i','h','t']:
                if c[l] == v:
                    del c[l]
                else:
                    c[l] -= v
        
        if 't' in c:
            v = c['t']
            ans += '3' * v
            del c['t']
            for l in ['r','h','r']:
                if c[l] == v:
                    del c[l]
                else:
                    c[l] -= v
            
            if c['e'] == 2*v:
                del c['e']
            else:
                c['e'] -= 2*v
        
        if 'i' in c:
            v = c['i']
            ans += '9' * v
            del c['i']
            for l in ['e']:
                if c[l] == v:
                    del c[l]
                else:
                    c[l] -= v
            
            if c['n'] == 2*v:
                del c['n']
            else:
                c['n'] -= 2*v

        return "".join(sorted(ans))
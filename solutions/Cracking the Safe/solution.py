# Problem: Cracking the Safe
# Language: python3
# Runtime: 80 ms
# Memory: 14.6 MB

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n==1:return ''.join(map(str,range(k)))
        seen, a=set(['0'*n]),['0'*n]
        for _ in range((k**n)-1):
            cur=a[-1]
            prefix=cur[1:]
            for x in range(k-1,-1,-1):
                if prefix+str(x) not in seen:
                    a.append(prefix+str(x))
                    seen.add(prefix+str(x))
                    break
        res=a[0]
        for n in a[1:]: res+=n[-1]
        return res
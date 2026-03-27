# Problem: Lexicographically Smallest Palindromic Permutation Greater Than Target
# Language: python3
# Runtime: 7 ms
# Memory: 18.1 MB

LC = 'abcdefghijklmnopqrstuvwxyz'
class Solution:
    def lexPalindromicPermutation(self, S: str, T: str) -> str:
        if len(T) == 1:
            if T[0] >= S[0]: return ""
            return S
        C = Counter(S)
        mid = ""
        L = []
        M = 0
        for k,v in C.items():
            if v & 1:
                if mid: return ""
                mid = k
                if v > 2:
                    L.append([k, v//2])
                    M += v // 2
            else:
                L.append([k, v//2])
                M += v // 2
        
        C = Counter()

        def make_max(C):
            ans = ""
            for x in LC:
                ans += C[x] * x
            return ans

        for k,v in L:
            C[k] = v
        
        keep = True
        ans = ""
        for i in range(M):
            
            if C[T[i]]:
                C[T[i]] -= 1
            else:
                ind = LC.index(T[i])
                for j in range(ind+1,26):
                    if C[LC[j]]:
                        C[LC[j]] -= 1
                        s = T[:i] + LC[j] + make_max(C)
                        return s + mid + s[::-1]
                keep = False
                break
        else:
            if T[:M] + mid + T[:M][::-1] > T: 
                return T[:M] + mid + T[:M][::-1]
        if keep:
            i+=1
        for k in range(i-1,-1,-1):
            
            C[T[k]] += 1
            # print(T[k], C)
            ind = LC.index(T[k])
            for j in range(ind+1,26):
                if C[LC[j]]:
                    C[LC[j]] -= 1
                    s = T[:k] + LC[j] + make_max(C)
                    return s + mid + s[::-1]
        return ""


        
                        

        
        
        
        
                
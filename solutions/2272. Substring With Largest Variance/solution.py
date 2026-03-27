# Problem: Substring With Largest Variance
# Language: python3
# Runtime: 8207 ms
# Memory: 14 MB

class Solution:
    def largestVariance(self, s: str) -> int:
        
        def count_variance(b = 'b', a = 'a'):
            curra = currb = na = nb = ans = 0
            for l in s:
                if l == b:
                    nb += 1
                    currb += 1
                    curra = 0
                    
                elif l == a:
                    curra += 1
                    if nb == currb and curra == 1:
                        # we need this condition to reset na for cases like
                        # abbbba if currb == nb means we can skip 'a's before
                        na = 0
                    
                    na += 1
                    if na > nb:
                        # Kadane part: 
                        # if we stocked with the case like bbbaaaa 
                        # no need to keep all 'a's and 'b's we should restart our counts
                        na = 1
                        nb = 0
                    currb = 0
                        
                if na and nb:
                    ans = max(ans, nb-na)
            return ans
        
        ans = 0
        for l1,l2 in permutations(set(s),2):
            ans = max(ans, count_variance(l1,l2))
        return ans
        
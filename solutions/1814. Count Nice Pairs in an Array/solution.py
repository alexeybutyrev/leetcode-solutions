# Problem: Count Nice Pairs in an Array
# Language: python3
# Runtime: 624 ms
# Memory: 26.9 MB

class Solution:
    def countNicePairs(self, A: List[int]) -> int:
        c = Counter()
        rev = lambda x: x - int(str(x)[::-1])
        ans =0
        for x in A:
            y = rev(x)
            ans+=c[y]
            ans%=10**9+7
            c[y]+=1
        return ans
# Problem: Largest Palindromic Number
# Language: python3
# Runtime: 118 ms
# Memory: 15.1 MB

class Solution:
    def largestPalindromic(self, num: str) -> str:
        c = Counter(num)
        
        
        left = ""
        right = ""
        center = ""
        for k in "9876543210":
            v = c[k]
            if v and v % 2 == 0:
                left = k * (v // 2) + left
                right += k * (v // 2)
            
            if v and v %2 !=0:
                v -= 1
                left = k * (v // 2) + left
                right += k * (v // 2)
                center = max(center,k)
        
        ans = (right + center + left).strip("0")
        if not ans:
            return "0"
        return ans
        
    
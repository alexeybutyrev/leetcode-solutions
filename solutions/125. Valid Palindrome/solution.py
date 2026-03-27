# Problem: Valid Palindrome
# Language: python3
# Runtime: 44 ms
# Memory: 14.4 MB

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start,end = ord('a'), ord('z')
        n = len(s)
        left, right = 0, n-1
        
        while left < right:
            
            while left < n and not s[left].isalnum():
                left+=1
                
            while right > 0 and not s[right].isalnum():
                right-=1
            
            #print(left, right)
            if left >= right:
                return True
            if s[right].lower() != s[left].lower():
                return False
            left += 1
            right -=1
        
        return True
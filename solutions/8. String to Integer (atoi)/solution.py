# Problem: String to Integer (atoi)
# Language: python3
# Runtime: 36 ms
# Memory: 14 MB

class Solution:
    def myAtoi(self, s: str) -> int:
        HI = (1 << 31) - 1
        LO = -(1 << 31)
        for i in range((N:=len(s))):
            l = s[i]
            if (s[i] == '+' or s[i] == '-') and i < N - 1 and s[i+1].isdigit():
                ans = 0
                i+=1
                while i < N and s[i].isdigit():
                    ans *= 10 
                    ans += int(s[i])
                    i += 1
                if l == "-":
                    return LO if -ans < LO else -ans
                else:
                    return HI if ans > HI else ans
                
            elif s[i].isdigit():                
                ans = 0
                while i < N and s[i].isdigit():
                    ans *= 10 
                    ans += int(s[i])
                    i += 1
                return HI if ans > HI else ans
            elif s[i] == ' ':
                continue
            else:
                return 0
        return 0
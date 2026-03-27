# Problem: Integer to Roman
# Language: python3
# Runtime: 13 ms
# Memory: 18 MB

class Solution:
    def intToRoman(self, num: int) -> str:
               
        ans = "" 
        
        S = str(num)
        
        N = len(S)
        
        for i in range(N):
            if S[i] in ['4', '9']:
                if N - i == 1:
                    l =  'IV' if S[i] == '4' else 'IX'
                if N - i == 2:
                    l =  'XL' if S[i] == '4' else 'XC'
                if N - i == 3:
                    l =  'CD' if S[i] == '4' else 'CM'
                ans = ans + l
            elif S[i] in ['1','2','3']:

                if N - i == 1:
                    l = 'I'
                if N - i == 2:
                    l = 'X'
                if N - i == 3:
                    l = 'C'
                if N -i == 4:
                    l = 'M'

                ans = ans + l * int(S[i])
                
            elif S[i] in ['5','6','7','8']:
                if N - i == 1:
                    l = 'V' + 'I' * (int(S[i]) - 5)
                if N - i == 2:
                    l = 'L' + 'X' * (int(S[i]) - 5)
                if N - i == 3:
                    l = 'D' + 'C' * (int(S[i]) - 5)    
                    
                ans = ans + l
        
        return ans
# Problem: Integer to English Words
# Language: python3
# Runtime: 32 ms
# Memory: 14.2 MB

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        d = {1: "One",
             2: "Two",
             3: "Three",
             4: "Four",
             5: "Five",
             6: "Six",
             7: "Seven",
             8: "Eight",
             9: "Nine",
             10: "Ten",
             11: "Eleven",
             12: "Twelve",
             13: "Thirteen",
             14: "Fourteen",
             15: "Fifteen",
             16: "Sixteen",
             17: "Seventeen",
             18: "Eighteen",
             19: "Nineteen",
             20: "Twenty",
             30: "Thirty",
             40: "Forty",
             50: "Fifty",
             60: "Sixty",
             70: "Seventy",
             80: "Eighty",
             90: "Ninety",
             0:  ""}


        def num2str(n):
            ans = ""
            h = n // 100
            if h:
                ans += d[h] + " Hundred"
            n %= 100

            if not n:
                return ans.lstrip(" ")

            if n in d:
                return (ans + " " +d[n]).lstrip(" ")

            t = n // 10
            if t:
                ans += " " + d[t * 10]
            n %= 10

            if n:
                ans += " " + d[n]

            return ans.lstrip(" ")

        ans = ""
        billions = num // 1000000000
        if billions:
            ans += d[billions] + " Billion"

        num %= 1000000000

        if not num:
            return ans.lstrip(" ")

        millions = num // 1000000

        if millions:
            ans += " " + num2str(millions) + " Million"
        num %= 1000000

        if not num:
            return ans.lstrip(" ")

        thousands = num // 1000

        if thousands:
            ans += " " + num2str(thousands) + " Thousand"
        num %= 1000

        if not num:
            return ans.lstrip(" ")

        ans += " " + num2str(num)

        return ans.lstrip(" ")

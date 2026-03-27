# Problem: Apply Discount to Prices
# Language: python3
# Runtime: 265 ms
# Memory: 16.7 MB

class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        #if discount == 0:
        #    return sentence
        
        ans = []
        for w in sentence.split(" "):
            if w.startswith("$") and w[1:].isnumeric():
                n = int(w[1:])
                number = round(n*(100-discount)/100,2) * 1.0
                s = f"${number:.2f}"
                ans.append(s)
            else:
                ans.append(w)
        
        return " ".join(ans)
                
                
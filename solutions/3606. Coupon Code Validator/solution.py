# Problem: Coupon Code Validator
# Language: python3
# Runtime: 15 ms
# Memory: 18.2 MB

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        c = defaultdict(list)
        for cd,b,ia in zip(code, businessLine, isActive):
            if ia and cd:
                for x in cd:
                    if x.isalpha() or x.isdigit() or x == "_":
                        continue
                    else:
                        break
                else:
                    c[b].append(cd)
        
        for x in c:
            c[x].sort()
        
        ANS = []
        for x in ["electronics", "grocery", "pharmacy", "restaurant"]:
            ANS += c[x]
        return ANS


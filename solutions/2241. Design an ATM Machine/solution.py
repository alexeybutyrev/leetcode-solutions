# Problem: Design an ATM Machine
# Language: python3
# Runtime: 853 ms
# Memory: 17.5 MB

class ATM:

    def __init__(self):
        self.c = [0] * 5
        self.val = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i,v in enumerate(banknotesCount):
            self.c[i] += v

    def withdraw(self, amount: int) -> List[int]:
        nc = deepcopy(self.c)
        ans = [0] * 5
        for i in range(4,-1,-1):
            
            if amount >= self.c[i] * self.val[i]:
                
                nc[i] = 0
                amount -= self.val[i] * self.c[i]
                ans[i] = self.c[i]
            else:
                if amount >= self.val[i]:
                    c = amount // self.val[i]
                    nc[i] -= c
                    amount -= c * self.val[i]
                    ans[i] = c
                else:
                    continue
                
                
            if not amount:
                self.c = deepcopy(nc)
                return ans
        return [-1]
                
                


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
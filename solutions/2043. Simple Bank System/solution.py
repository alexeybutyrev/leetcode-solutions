# Problem: Simple Bank System
# Language: python3
# Runtime: 15 ms
# Memory: 47.7 MB

class Bank:

    def __init__(self, balance: List[int]):
        self.b = balance
        self.N = len(balance)
        
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        
        if account1 > self.N or account1 <= 0 or account2 > self.N or account2 <= 0:
            return False
        
        if money == 0:
            return True
        a1 = account1 -1
        a2 = account2 -1
        if self.b[a1] >= money:
            self.b[a1] -= money
            self.b[a2] += money
        else:
            return False
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account > self.N or account <= 0:
            return False
        
        self.b[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > self.N or account <= 0:
            return False
        if self.b[account - 1] < money:
            return False
        self.b[account - 1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
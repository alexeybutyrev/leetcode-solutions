# Problem: Design Spreadsheet
# Language: python3
# Runtime: 67 ms
# Memory: 23.6 MB

class Spreadsheet:

    def __init__(self, rows: int):
        self.c = defaultdict(lambda: 0)

    def setCell(self, cell: str, value: int) -> None:
        self.c[cell] = value

    def resetCell(self, cell: str) -> None:
        self.c[cell] = 0

    def getValue(self, formula: str) -> int:
        a,b = formula.split("+")
        a = a[1:]
        ans = 0
        if a[0].isalpha(): 
            ans += self.c[a]
        else:
            ans += int(a)
        if b[0].isalpha(): 
            ans += self.c[b]
        else:
            ans += int(b)
        return ans



# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
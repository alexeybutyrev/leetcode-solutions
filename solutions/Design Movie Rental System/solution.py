# Problem: Design Movie Rental System
# Language: python3
# Runtime: 612 ms
# Memory: 114 MB

from sortedcontainers import SortedSet
class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        for x in entries:
            print(x)
        self.R = SortedSet()
        self.N = 5
        self.M = defaultdict(SortedList)
        self.P = {}

        for s,m,p in entries:
            self.M[m].add((p,s))
            self.P[(m,s)] = p

    def search(self, movie: int) -> List[int]:
        return [s for _,s in self.M[movie][0:self.N]]

    def rent(self, shop: int, movie: int) -> None:
        p = self.P[(movie,shop)]
        self.M[movie].remove((p,shop))
        self.R.add((p,shop,movie))        

    def drop(self, shop: int, movie: int) -> None:
        p = self.P[(movie,shop)]
        if (p,shop,movie) in self.R:
            self.R.remove((p,shop,movie))

        self.M[movie].add((p,shop))

    def report(self) -> List[List[int]]:
        return [[s,m] for p,s,m in self.R[0:self.N]]
            


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
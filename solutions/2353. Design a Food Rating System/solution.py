# Problem: Design a Food Rating System
# Language: python3
# Runtime: 227 ms
# Memory: 49.4 MB

from sortedcontainers import SortedList
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.d = defaultdict(SortedList)
        self.scores = {}
        self.c = {}
        for f,c,r in zip(foods,cuisines,ratings):
            self.d[c].add((-r,f))
            self.scores[f] = r
            self.c[f] = c
            

    def changeRating(self, food: str, newRating: int) -> None:
        self.d[self.c[food]].remove((-self.scores[food],food))
        self.scores[food] = newRating
        self.d[self.c[food]].add((-self.scores[food],food))

    def highestRated(self, cuisine: str) -> str:
        return self.d[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
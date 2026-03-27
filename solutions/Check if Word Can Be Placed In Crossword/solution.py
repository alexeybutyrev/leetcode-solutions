# Problem: Check if Word Can Be Placed In Crossword
# Language: python3
# Runtime: 1364 ms
# Memory: 27 MB

class Solution:
    def placeWordInCrossword(self, A: List[List[str]], word: str) -> bool:
        def check(word):
            N = len(A)
            M = len(A[0])
            S0 = len(word)

            def check_front(i,j):
                for dx,dy in {(0,1)}:
                    x = i + dx
                    y = j + dy
                    if x >= 0 and x < N and y >= 0 and y < M and A[x][y] != "#":
                        return False
                return True

            def check_down(i,j):
                for dx,dy in {(1,0)}:
                    x = i + dx
                    y = j + dy
                    if x >= 0 and x < N and y >= 0 and y < M and A[x][y] != "#":
                        return False
                return True

            def dfs_front(i,j):
                size = 0
                for k in range(j,M):
                    if size == S0:
                        return check_front(i,k-1)
                    if A[i][k] == " " or A[i][k] == word[size]:
                        size += 1
                    else:
                        return False

                return size == S0 and check_front(i,k)

            def dfs_down(i,j):
                size = 0
                for k in range(i,N):

                    if size == S0:
                        return check_down(k-1,j)
                    if A[k][j] == " " or A[k][j] == word[size]:
                        size += 1
                    else:
                        return False
                return size == S0 and check_down(k,j)

            for i in range(N):
                for j in range(M):
                    if A[i][j] == " " or A[i][j] == word[0]:
                        if (j == 0 or A[i][j-1] == "#") and dfs_front(i,j):
                            return True
                        if (i== 0 or A[i-1][j] == "#") and dfs_down(i,j):
                            return True

            return False
        return check(word) or check(word[::-1])
import time


def is_promising(s):
    return all(s[i] != s[j] and j - i != abs(s[i] - s[j]) for i in range(len(s)) for j in range(i + 1, len(s)))


class NQueensSolverRecursive:
    def __init__(self, n):
        self.n = n

    def is_complete(self, s):
        return len(s) == self.n

    def backtracking(self, s):

        if self.is_complete(s):
            return s

        for row in range(self.n):
            news = s + [row]
            if is_promising(news):
                found = self.backtracking(news)
                if found != None:
                    return found

        return None

    def solve(self):
        return self.backtracking([])


class AllSolutionsRecursive(NQueensSolverRecursive):

    def __init__(self, n):
        super().__init__(n)

    def backtracking(self, s):
        if len(s) == self.n:
            yield s

        for row in range(self.n):
            new_s = s+[row]
            if is_promising(new_s):
                for solution in self.backtracking(new_s):
                    yield solution

    def solve(self):

        solutions = []
        for solution in self.backtracking([]):
            solutions.append(solution)
        return solutions

if __name__ == '__main__':

    for i in range(4,7):
        Solver = AllSolutionsRecursive(i)
        timer = time.time()
        solutions = Solver.solve()
        timer2 = time.time()
        print('Time:', timer2-timer)
        print('Solutions:', solutions,)



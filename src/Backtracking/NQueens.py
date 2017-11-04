
def is_promising(s):
    new_row = len(s)-1
    return all(s[new_row] != s[i] and new_row - i != abs(s[new_row] - s[i]) for i in range(new_row))


class NQueensSolverIterative:

    def __init__(self, n):
        self.n = n

    def is_complete(self, s):
        return len(s) == self.n

    def backtracking(self, s):

        if not s:
            stack = [None]
        else:
            stack = s

        while len(stack) > 0:

            q = stack.pop()
            if q is None:
                i = 0
            else:
                i = q + 1

            while i < self.n:
                q = i
                i += 1
                aux = stack + [q]
                if is_promising(aux):
                    stack.append(q)
                    if len(stack) == self.n:
                        return stack
                    stack.append(None)
                    break
        return None

    def solve(self):
        return self.backtracking([])




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
                if found is not None:
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


class NQueensSolverRecursiveHeap(NQueensSolverRecursive):

    def __init__(self, n):
        super().__init__(n)

    def backtracking(self, s):
        stack = s
        if len(s) == self.n:
            return s

        for row in range(self.n):
            stack.append(row)
            if is_promising(stack):
                found = self.backtracking(stack)
                if found is not None:
                    return found
                else:
                    stack.pop()
            else:
                stack.pop()

        return None

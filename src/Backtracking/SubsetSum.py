def branch(array):
    return [array+[0],array+[1]]


class SubsetSumRecursive:

    def __init__(self, s, w):
        self.s = s
        self.w = w

    def is_complete(self, array):
        return len(array) == len(self.s)

    def is_feasible(self, array):
        weight = 0
        for i in range(len(self.s)):
            weight += array[i]*self.s[i]
        return weight == self.w

    def is_promising(self, array):
        weight = 0
        for i in range(len(array)):
            weight = array[i] * self.s[i]
        return weight < self.w

    def backtracking(self, array):

        if self.is_complete(array):
            if self.is_feasible(array):
                return array
        else:
            children = branch(array)
            for child in children:
                if self.is_promising(child):
                    found = self.backtracking(child)
                    if found is not None:
                        return found

        return None

    def solve(self):
        return self.backtracking([])

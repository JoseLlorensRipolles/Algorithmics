class SubsetSumRecursiveNotOptimal:

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

    def branch(self, array):
        return [array[1], array + [0]]

    def backtracking(self, array):

        if self.is_complete(array):
            if self.is_feasible(array):
                return array
        else:
            children = self.branch(array)
            for child in children:
                if self.is_promising(child):
                    found = self.backtracking(child)
                    if found is not None:
                        return found

        return None

    def solve(self):
        return self.backtracking([])


class SubsetSumRecursive:
    def __init__(self, s, w):
        self.sequence = s
        self.max_weight = w

    def is_complete(self, state):
        return len(state[0]) == len(self.sequence)

    def is_feasible(self, state):
        return state[1] == self.max_weight

    def is_promising(self, state):
        return state[1] <= self.max_weight <= state[1] + state[2]

    def branch(self, state):
        new_element_weight = self.sequence[len(state[0])]
        aux1 = state[0] + [1]
        aux2 = state[0] + [0]
        return [(aux1, state[1] + new_element_weight, state[2] - new_element_weight),
                (aux2, state[1], state[2] - new_element_weight)]

    def complete(self, state):
        for i in range(len(state[0]), len(self.sequence)):
            state[0].append(0)
        return state

    def backtracking(self, state):
        if self.is_complete(state):
            if self.is_feasible(state):
                return state
        else:
            if self.is_feasible(state):
                return self.complete(state)

            children = self.branch(state)
            for child in children:
                if self.is_promising(child):
                    found = self.backtracking(child)
                    if found is not None:
                        return found

        return None

    def solve(self):
        self.sequence = sorted(self.sequence)
        array = self.backtracking(([], 0, sum(self.sequence)))[0]
        res = set()
        for i in range(len(array)):
            if array[i] == 1:
                res.add(self.sequence[i])
        return res




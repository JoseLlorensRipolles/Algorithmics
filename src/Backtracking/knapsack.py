import heapq
import math

class KnapsackSolverBranchAndBoundScheme:

    def __init__(self, max_weight, objects):
        self.w = [x[0] for x in objects]
        self.v = [x[1] for x in objects]
        self.max_weight = max_weight

    def solve(self):
        states = []
        heapq.heappush(states, (math.inf, []))
        x = None
        fx = -math.inf

        while len(states) != 0:
            (score_s, s) = heapq.heappop(states)
            for child in self.branch(s):
                if self.is_promising(child):
                    if self.is_completed(child):
                        if self.score(child) > fx:
                            x = child
                            fx = self.score(child)
                            states = self.prune(states)
                    else:
                        if self.optimistic_score(child) >= fx:
                            heapq.heappush(states, (self.optimistic_score(child), child))

        return x



if __name__ == '__main__':
    objects = [(1, 8), (2, 4), (3, 0), (2, 5), (2, 3)]
    max_weight = 4
    KnapsackSolverBranchAndBoundScheme(max_weight, objects)

import time


class DiscountCard:

    def __init__(self):
        self.res = []
        self.p = []
        self.target_price = 0
        self.c = []
        self.target_kal = 0
        self.actual_price = 0
        self.actual_kal = 0
        self.remaining_kal = 0
        self.remaining_price = 0

    def is_complete(self, i):
        return i == len(self.p)

    def is_feasible(self):
        return self.actual_kal == self.target_kal and self.actual_price == self.target_price

    def is_promising(self):

        return self.actual_kal <= self.target_kal and self.actual_price <= self.target_price and self.remaining_kal +\
               self.actual_kal >= self.target_kal and self.remaining_price + self.actual_price >= self.target_price

    def branch(self, i):
        for j in {0, 1}:
            self.res[i] = j
            yield

    def backtracking(self, i):

        if self.is_complete(i):
            if self.is_feasible():
                return self.res
        else:
            for child in self.branch(i):
                self.actual_price += self.res[i]*self.p[i]
                self.actual_kal += self.res[i]*self.c[i]
                self.remaining_price -= self.p[i]
                self.remaining_kal -= self.c[i]

                if self.is_promising():
                    found = self.backtracking(i+1)
                    if found is not None:
                        return found

                self.actual_price -= self.res[i] * self.p[i]
                self.actual_kal -= self.res[i] * self.c[i]
                self.remaining_price += self.p[i]
                self.remaining_kal += self.c[i]
        return None

    def solve(self, vp, vc, p, c):
        self.p = vp
        self.c = vc
        self.target_price = p
        self.target_kal = c
        self.remaining_kal = sum(self.c)
        self.remaining_price = sum(self.p)
        for i in range(len(self.p)):
            self.res.append(0)

        return self.backtracking(0)


if __name__ == '__main__':
    solver = DiscountCard()
    print(solver.solve([5, 3, 4, 2, 1], [200, 110, 100, 80, 50], 10, 350))

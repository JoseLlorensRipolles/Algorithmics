import unittest
import src.Backtracking.NQueens as NQueens


class NQueensTest(unittest.TestCase):

    def test_iterative_solution(self):

        solver = NQueens.NQueensSolverIterative(8)
        solution = solver.solve()
        self.assertEqual(len(solution), 8)
        self.assertEqual(all(solution[i] != solution[j] and j - i != abs(solution[i] - solution[j]) for i in range(8) for j in
                    range(i + 1, 8)), True)


if __name__ == '__main__':
    unittest.main()
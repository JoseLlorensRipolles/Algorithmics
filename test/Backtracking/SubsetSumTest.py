import unittest
import src.Backtracking.SubsetSum as SubsetSum


class SubsetSumTest(unittest.TestCase):

    def test_recursive_solution(self):
        solver = SubsetSum.SubsetSumRecursive([4, 5, 3, 6], 8)
        self.assertEqual(solver.solve(), {3, 5})

if __name__ == '__main__':
    unittest.main()

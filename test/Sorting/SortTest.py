import random
import unittest

from src.Sorting import *


class TestSortingMethods(unittest.TestCase):

    def setUp(self):
        self.unsorted_sequence = []
        for i in range(1000):
            self.unsorted_sequence.append(random.randint(-1000, 1000))

    def test_insertion(self):
        self.assertEqual(sorted(self.unsorted_sequence), InsertionSort.sort(self.unsorted_sequence))

    def test_bubble(self):
        self.assertEqual(sorted(self.unsorted_sequence), BubbleSort.sort(self.unsorted_sequence))

    def test_selection(self):
        self.assertEqual(sorted(self.unsorted_sequence), SelectionSort.sort(self.unsorted_sequence))

    def test_shell(self):
        self.assertEqual(sorted(self.unsorted_sequence), ShellSort.sort(self.unsorted_sequence))

    def test_merge(self):
        self.assertEqual(sorted(self.unsorted_sequence), MergeSort.sort(self.unsorted_sequence))

if __name__ == '__main__':
    unittest.main()

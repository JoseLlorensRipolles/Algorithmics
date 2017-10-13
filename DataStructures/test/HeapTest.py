import random
import unittest
from DataStructures.src.Heap import Heap


class HeapTest(unittest.TestCase):

    def test_getter(self):

        heap = Heap()
        self.assertEqual(heap.get_heap(), [])

    def test_sift_up(self):

        values = [10, 5, 7, 12, 3, 2, 4]
        correct_heap = [12, 10, 7, 5, 3, 2, 4]
        self.assertEqual(Heap.sift_up(values, 3), correct_heap)

        values = [10, 5, 7, 8, 3, 2, 4]
        correct_heap = [10, 8, 7, 5, 3, 2, 4]
        self.assertEqual(Heap.sift_up(values, 3), correct_heap)

        self.assertEqual(Heap.sift_up([], 1), [])

        values = [10, 8, 7, 5, 3, 2, 4]
        self.assertEqual(Heap.sift_up(values, 7), values)

    def test_init(self):

        heap = Heap([7, 2, 43, 52, 24, 32, 35, 14, 31, 57, 79, 3, 66, 6, 45])
        correct_heap_array = [79, 57, 66, 31, 52, 35, 45, 2, 14, 24, 43, 3, 7, 6, 32]
        self.assertEqual(heap.get_heap(), correct_heap_array)

    def test_insert(self):

        heap = Heap([7, 2, 43, 52, 24, 32, 35, 14, 31, 57, 79, 3, 66, 6, 45])
        heap.insert(78)
        correct_heap_array = [79, 78, 66, 57, 52, 35, 45, 31, 14, 24, 43, 3, 7, 6, 32, 2]
        self.assertEqual(heap.get_heap(), correct_heap_array)

        heap = Heap([])
        heap.insert(90)
        correct_heap_array = [90]
        self.assertEqual(heap.get_heap(),correct_heap_array)

    def test_find_max(self):

        values = [random.randint(0, 1000) for r in range(10000)]
        heap = Heap(values)
        self.assertEqual(heap.find_max(), max(values))


if __name__ == '__main__':
    unittest.main()

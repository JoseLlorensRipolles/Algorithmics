import unittest
import DataStructures.src.Heap as Heap


class HeapTest(unittest.TestCase):

    def test_getter(self):
        heap = Heap()
        self.assertEqual(heap.get_heap(), "")


if __name__ == '__main__':
    unittest.main()
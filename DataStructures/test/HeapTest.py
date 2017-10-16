import random
import unittest
from DataStructures.src.Heap import Heap
from DataStructures.test.HeapStub import HeapStub


class HeapTest(unittest.TestCase):

    def test_getter(self):

        heap = Heap()
        self.assertEqual(heap.get_heap(), [])

    def test_sift_up(self):

        heap_stub = HeapStub([10, 5, 7, 12, 3, 2, 4])
        correct_res = [12, 10, 7, 5, 3, 2, 4]
        heap_stub.sift_up(3)
        self.assertEqual(heap_stub.get_heap(), correct_res)

        heap_stub = HeapStub([10, 5, 7, 8, 3, 2, 4])
        correct_res = [10, 8, 7, 5, 3, 2, 4]
        heap_stub.sift_up(3)
        self.assertEqual(heap_stub.get_heap(), correct_res)

        heap_stub = HeapStub([])
        heap_stub.sift_up(1)
        self.assertEqual(heap_stub.get_heap(), [])

        heap_stub = HeapStub([10, 8, 7, 5, 3, 2, 4])
        heap_stub.sift_up(7)
        self.assertEqual(heap_stub.get_heap(), [10, 8, 7, 5, 3, 2, 4])
        
    def test_sift_down(self):

        heap_stub = HeapStub([3, 57, 66, 31, 52, 35, 45, 2, 14, 24, 43, 3, 7, 6])
        correct_res = [66, 57, 45, 31, 52, 35, 6, 2, 14, 24, 43, 3, 7, 3]
        heap_stub.sift_down(0)
        self.assertEqual(heap_stub.get_heap(), correct_res)

        heap_stub = HeapStub([5, 9, 8, 7, 6])
        correct_res = [9, 7, 8, 5, 6]
        heap_stub.sift_down(0)
        self.assertEqual(heap_stub.get_heap(), correct_res)

        heap_stub = HeapStub([3, 8, 9, 7, 6])
        correct_res = [9, 8, 3, 7, 6]
        heap_stub.sift_down(0)
        self.assertEqual(heap_stub.get_heap(), correct_res)

        heap_stub = HeapStub([-2, 9, 8, 7, 5, 4, 3])
        correct_res = [9, 7, 8, -2, 5, 4, 3]
        heap_stub.sift_down(0)
        self.assertEqual(heap_stub.get_heap(), correct_res)

        heap_stub = HeapStub([-222, -569, -72, -930, -628, -111])
        correct_res = [-72, -569, -111, -930, -628, -222]
        heap_stub.sift_down(0)
        self.assertEqual(heap_stub.get_heap(), correct_res)

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
        self.assertEqual(heap.get_heap(), correct_heap_array)

    def test_find_max(self):

        values = [random.randint(-1000, 1000) for r in range(100)]
        heap = Heap(values)
        self.assertEqual(heap.find_max(), max(values))

    def test_get_size(self):

        heap = Heap([])
        self.assertEqual(heap.get_size(), 0)

        for i in range(10):
            heap.insert(i)

        self.assertEqual(heap.get_size(), 10)

        heap = Heap([random.randint(-1000, 1000) for r in range(100)])
        self.assertEqual(heap.get_size(), 100)

    def test_pop(self):
        values = [random.randint(-1000, 1000) for r in range(10)]
        heap = Heap(values)

        for i in range(heap.get_size()):
            max_value = max(values)
            self.assertEqual(max_value, heap.pop())
            values.remove(max_value)

    #TODO
    def test_merge(self):
        heap = Heap([1, 3, 6, 4, 3])
        heap2 = Heap([5, 7, 9])
        heap.merge()
        self.assertEqual()


if __name__ == '__main__':
    unittest.main()

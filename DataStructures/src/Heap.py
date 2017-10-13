class Heap:

    def __init__(self, array=[]):

        self.array = []

        for i in range(len(array)):
            self.array.append(array[i])
            self.array = Heap.sift_up(self.array, i)

    @staticmethod
    def sift_up(array, i):

        if (len(array) is 0) or i >= len(array):
            return array

        while array[int((i-1)/2)] < array[i]:
            father = int((i-1)/2)
            aux = array[i]
            array[i] = array[father]
            array[father] = aux
            i = father

        return array

    def get_heap(self):
        return self.array

    def insert(self, new_value):
        self.array.append(new_value)
        self.array = Heap.sift_up(self.array, len(self.array)-1)

    def find_max(self):

        if self.array is []:
            return None

        return self.array[0]




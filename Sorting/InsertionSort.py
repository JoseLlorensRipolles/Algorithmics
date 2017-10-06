import sys


def insertion_sort(sequence):

    # For each element, e1. We start with 1, this way the initial list is sorted.
    for i in range(1, len(sequence)):

        # We search backwards a element e2 minor than e1, because the list from 0 to i is sorted, the fist minor element
        # will be the greatest of them. Each time we go backwards if e2 is greater than e1 we copy it on the right
        # adjacent position, this way when we find the minor element we just copy  e1 at e2 position +1

        for j in range(i, 0, -1):
            if sequence[j-1] > sequence[j]:
                aux = sequence[j-1]
                sequence[j-1] = sequence[j]
                sequence[j] = aux
            else:
                break

    return sequence

if __name__ == "__main__":
    sequence_input = sys.argv[1:len(sys.argv)]
    sequence_parsed = list(map(int, sequence_input))
    print(insertion_sort(sequence_parsed))

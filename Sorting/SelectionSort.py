import sys
import math


def sort(sequence):

    # For each element e1 in position i
    for i in range(len(sequence)):
        e1 = sequence[i]
        e2 = math.inf
        e2_index = -1

        # We search for the minimum element from i to the end of the list.
        for j in range(i, len(sequence)):
            if sequence[j] < e2:
                e2 = sequence[j]
                e2_index = j

        # We change this to elements for each other.
        sequence[i] = e2
        sequence[e2_index] = e1

    return sequence

if __name__ == "__main__":
    sequence_input = sys.argv[1:len(sys.argv)]
    sequence_parsed = list(map(int, sequence_input))
    print(sort(sequence_parsed))

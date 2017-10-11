import sys


def sort(sequence):
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        for i in range(gap, len(sequence)):
            aux = sequence[i]

            for j in range(i, gap-1, -gap):
                if sequence[j-gap] <= aux:
                    break
                else:
                    sequence[j] = sequence[j-gap]

            # Because range function does not decrease j value in the last iteration we must check it and decrease the
            # value if needed.
            if sequence[j-gap] > aux:
                j -= gap
            sequence[j] = aux

    return sequence


if __name__ == "__main__":
    sequence_input = sys.argv[1:len(sys.argv)]
    sequence_parsed = list(map(int, sequence_input))
    print(sort(sequence_parsed))


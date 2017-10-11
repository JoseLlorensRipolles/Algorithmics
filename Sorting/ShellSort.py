import sys


def sort(sequence):
    gaps = [4, 1]
    # gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        for i in range(gap, len(sequence)):
            aux = sequence[i]

            for j in range(i, gap-2, -gap):
                if sequence[j-gap] <= aux:
                    break
                else:
                    sequence[j] = sequence[j-gap]
            sequence[j] = aux

    return sequence


if __name__ == "__main__":
    sequence_input = sys.argv[1:len(sys.argv)]
    sequence_parsed = list(map(int, sequence_input))
    print(sort([3, 1, 65, 234, 2, 34, 764, 234, 365, 7, 345, 47, 24, 653, 76, 254, 356, 645, 3, 24, 476, 78, 35, 24]))


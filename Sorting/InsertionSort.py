import sys


def insertion_sort(sequence):

    for i in range(1, len(sequence)):
        for j in range(i, 0, -1):
            if sequence[j-1] > sequence[j]:
                aux = sequence[j-1]
                sequence[j-1] = sequence[j]
                sequence[j] = aux
            else:
                break

    return sequence

if __name__ == "__main__":
    sequence = sys.argv[1:len(sys.argv)]
    sequence = list(map(int, sequence))
    print(insertion_sort(sequence))

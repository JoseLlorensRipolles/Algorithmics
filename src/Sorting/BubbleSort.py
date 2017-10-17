import sys


def sort(sequence):

    # While there are errors
    errors = True
    while errors:
        errors = False

        # We iterate sequence and averi pair of elements i, i+1 if they are wrongly sorted we switch them.
        for i in range(len(sequence)-1):
            if sequence[i] > sequence[i+1]:
                aux = sequence[i]
                sequence[i] = sequence[i+1]
                sequence[i+1] = aux
                errors = True

    return sequence

if __name__ == "__main__":
    sequence_input = sys.argv[1:len(sys.argv)]
    sequence_parsed = list(map(int, sequence_input))
    print(sort(sequence_parsed))

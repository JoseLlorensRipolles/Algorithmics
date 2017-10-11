import sys


# Merging two sorted sequences has a linear time complexity, that is why this algorithm is n log(n). The merging is
# the N
def merge(sequence1, sequence2):
    i1 = 0
    i2 = 0
    sequence = []

    while i1 < len(sequence1) and i2 < len(sequence2):
        if sequence1[i1] < sequence2[i2]:
            sequence.append(sequence1[i1])
            i1 += 1
        else:
            sequence.append(sequence2[i2])
            i2 += 1

    if i1 < len(sequence1):
        sequence.extend(sequence1[i1:])
    else:
        sequence.extend(sequence2[i2:])

    return sequence


# We divide each sequence in two halves. We sort each half and then merge them. This has a log(n) complexity.
def sort(sequence):
    l = len(sequence)
    if l <= 1:
        return sequence
    else:
        return merge(sort(sequence[0:int(l/2)]), sort(sequence[int(l/2):l]))

if __name__ == "__main__":
    sequence_input = sys.argv[1:len(sys.argv)]
    sequence_parsed = list(map(int, sequence_input))
    print(sort([]))

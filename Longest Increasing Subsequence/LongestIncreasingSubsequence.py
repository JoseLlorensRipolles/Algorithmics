import sys


def longest_increasing_subsequence_n_2(sequence):

    # Result subsequence of the algorithm
    subsequence = []

    # List holding the size of the longest possible increasing subsequence ending in index element
    longest_subsequence_sizes = [1]

    # List to control backpointers, used for recreating the subsequence
    backpointers = [-1]

    global_longest_subsequence_size = -1
    index_subsequence_end = -1

    # We calculate the size of the longest possible increasing subsequence ending in each element
    for i in range(1, len(sequence)):
        longest_subsequence_size = 1
        backpointer = -1

        # By lucking at the previous elements, we choose the one that, being minor than the element[i],
        # has the highest increasing subsequence size. Once we have this element[j], the size of the longest
        # increasing subsequence ending in element[i] will be the size of the longest increasing subsequence ending
        # in element[j] +1. We also set the element[i] backpointer to point at the element[j]
        for j in reversed(range(i)):
            if sequence[i] > sequence[j] and longest_subsequence_sizes[j] >= longest_subsequence_size:
                backpointer = j
                longest_subsequence_size = longest_subsequence_sizes[j]+1

        longest_subsequence_sizes.append(longest_subsequence_size)
        backpointers.append(backpointer)

        # If needed we actualise the global maximum and its index
        if longest_subsequence_size > global_longest_subsequence_size:
            global_longest_subsequence_size = longest_subsequence_size
            index_subsequence_end = i

    # We backtrack the backpointers in order to build the subsequence
    for i in range(longest_subsequence_sizes[index_subsequence_end]):
        subsequence.append(sequence[index_subsequence_end])
        index_subsequence_end = backpointers[index_subsequence_end]

    return subsequence


def longest_increasing_subsequence_n_log_n(sequence):

    # List holding the minimum number with the longest possible increasing subsequence size equal to index
    min_number = [sequence[0]]

    # List holding the size of the longest possible increasing subsequence ending in index element
    longest_subsequence_sizes = [1]

    # We calculate the size of the longest possible increasing subsequence ending in each element
    for i in range(1, len(sequence)):
        elem = sequence[i]
        end = False

        # We iterate backwards the min_number list. The first element we find that is minor that elem will be
        # its predecessor in the longest increasing subsequence. One we find it we actualise the list of sizes
        # and, if needed the min_numbers list.
        for j in reversed(range(len(min_number))):
            if elem > min_number[j]:
                end = True
                longest_subsequence_sizes.append(j + 2)
                if j + 1 == len(min_number):
                    min_number.append(elem)
                else:
                    if min_number[j+1] > elem:
                        min_number[j+1] = elem
                break
        if elem < min_number[0]:
            min_number[0] = elem
        if not end:
            longest_subsequence_sizes.append(1)

    subsequence = min_number
    return subsequence


if __name__ == '__main__':
    sequence_input = sys.argv[1:len(sys.argv)]
    sequence_parsed = list(map(int, sequence_input))
    print(longest_increasing_subsequence_n_log_n(sequence_parsed))

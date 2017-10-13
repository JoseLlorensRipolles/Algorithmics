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

    # List holding a tuple with the minimun number with a subsequence with size #index
    min_numbers = [(sequence[0], 0)]

    # List holding de size of the longest possible subsequence ending in #index element
    longest_subsequence_size = [1]

    # Lista holding backpointesr, used later to build the subsequence
    back_pointers = [-1]

    # Calculate the longest subsequence endieng in element #index
    for i in range(1, len(sequence)):

        elem = sequence[i]
        end = False
        back_pointers.append([-1])
        subsequence = []

        # We iterate backwards on the minimun mubers list. The first element minor than element #i will be his
        # predecesor in the longest subsequence. Once we find it we actualise the array holding the sizes and the
        # backpointers and, if needed, we actualize the min numbers list.

        for j in reversed(range(len(min_numbers))):
            if elem > min_numbers[j][0]:

                end = True
                longest_subsequence_size.append(j + 2)
                back_pointers[i] = min_numbers[j][1]

                if j + 1 == len(min_numbers):
                    min_numbers.append((elem, i))
                else:
                    if min_numbers[j+1][0] > elem:
                        min_numbers[j+1] = (elem, i)
                break
        if elem < min_numbers[0][0]:
            min_numbers[0] = (elem, i)
        if not end:
            longest_subsequence_size.append(1)

    index = min_numbers[-1][1]
    subsequence_size = longest_subsequence_size[index]

    for i in range(subsequence_size):
        subsequence.append(sequence[index])
        index = back_pointers[index]

    return subsequence[::-1]


if __name__ == '__main__':
    sequence_input = sys.argv[1:len(sys.argv)]
    sequence_parsed = list(map(int, sequence_input))
    print(longest_increasing_subsequence_n_log_n(sequence_parsed))

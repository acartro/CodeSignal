def first_bad_pair(sequence):
    """Return the first index of a pair of elements where the earlier
    element is not less than the later elements. If no such pair
    exists, return -1."""
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return i
    return -1


def almostIncreasingSequence(sequence):
    """Return whether it is possible to obtain a strictly increasing
    sequence by removing no more than one element from the array."""
    j = first_bad_pair(sequence)
    if j == -1:
        return True  # List is increasing
    if first_bad_pair(sequence[j-1:j] + sequence[j+1:]) == -1:
        return True  # Deleting earlier element makes increasing
    if first_bad_pair(sequence[j:j+1] + sequence[j+2:]) == -1:
        return True  # Deleting later element makes increasing
    return False  # Deleting either does not make increasin


sequence = [1, 3, 2, 0]  # false
almostIncreasingSequence(sequence)
sequence = [3, 5, 67, 98, 3]
almostIncreasingSequence(sequence)

# sequence = [1, 3, 2, 1]  # false
# almostIncreasingSequence(sequence)

# sequence = [1, 3, 2]  # true
# almostIncreasingSequence(sequence)

# sequence = [10, 1, 2, 3, 4, 5]  # true
# almostIncreasingSequence(sequence)

# sequence = [0, -2, 5, 6]  # true
# almostIncreasingSequence(sequence)

# sequence = [1, 1]  # true
# almostIncreasingSequence(sequence)

# sequence = [3, 6, 5, 8, 10, 20, 15]  # false
# almostIncreasingSequence(sequence)

# sequence = [1, 2, 1, 2]  # false
# almostIncreasingSequence(sequence)

# sequence = [1, 3, 2]  # true
# almostIncreasingSequence(sequence)

# sequence = [10, 1, 2, 3, 4, 5]  # true
# almostIncreasingSequence(sequence)

# sequence = [1, 2, 5, 3, 5]  # true
# almostIncreasingSequence(sequence)

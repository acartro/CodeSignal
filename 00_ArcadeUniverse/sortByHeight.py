# Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

# Example

# For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
# sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

# personal
def sortByHeight(a):
    pos = [i for i in range(len(a)) if a[i] == -1]
    a = [i for i in sorted(a) if (i != -1)]
    for i in range(len(pos)):
        a.insert(pos[i], -1)
    return a


a = [-1, 150, 190, 170, -1, -1, 160, 180]
sortByHeight(a)  # [-1, 150, 160, 170, -1, -1, 180, 190]

# best solution


def sortByHeight(a):

    l = sorted([i for i in a if i > 0])
    for n, i in enumerate(a):
        if i == -1:
            l.insert(n, i)
    return l

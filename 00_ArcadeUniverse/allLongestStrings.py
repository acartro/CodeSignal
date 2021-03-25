# Given an array of strings, return another array containing all of its longest strings.

# Example

# For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
# allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

# my function
def allLongestStrings(inputArray):
    m = max([len(i) for i in inputArray])
    return [j for i, j in enumerate(inputArray) if len(inputArray[i]) == m]

# other user
# def allLongestStrings(inputArray):
#     return [i for i in inputArray if len(i) == len(max(inputArray, key=len))]


if __name__ == "__main__":
    inputArray = ["enyky", "benyky", "yely", "varennyky"]
    print(
        f'inputArray = ["enyky","benyky","yely","varennyky"]: {allLongestStrings(inputArray)}')
    inputArray = ["aba", "aa", "ad", "vcd", "aba"]
    print(
        f'inputArray = ["aba", "aa", "ad", "vcd", "aba"]: {allLongestStrings(inputArray)}')
    inputArray = ["aa"]
    print(
        f'inputArray = ["aa"]: {allLongestStrings(inputArray)}')
    inputArray = ["a", "abc", "cbd", "zzzzzz",
                  "a", "abcdef", "asasa", "aaaaaa"]
    print(
        f'inputArray=["a", "abc", "cbd", "zzzzzz","a", "abcdef", "asasa", "aaaaaa"]: {allLongestStrings(inputArray)}')

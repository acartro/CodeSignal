# Given two strings, find the number of common characters between them.

# Example

# For s1 = "aabcc" and s2 = "adcaa", the output should be
# commonCharacterCount(s1, s2) = 3.

# Strings have 3 common characters - 2 "a"s and 1 "c".


# personal
def commonCharacterCount(s1, s2):
    dict1 = {char: s1.count(char) for char in s1}
    dict2 = {char: s2.count(char) for char in s2}
    sum = 0
    for key1 in dict1.keys():
        for key2 in dict2.keys():
            if(key1 == key2):
                sum = sum+min(dict1[key1], dict2[key2])
    return sum


# best solution
def commonCharacterCount(s1, s2):
    return sum([min(s1.count(i), s2.count(i)) for i in set(s1)])

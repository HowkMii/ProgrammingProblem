# Write a function that takes in an string and returns an the most frequent char.
# The string can be a whole sentence and should ignore the chars that aren't a letter or digit.
# Sample input: mississippis
# Sample output: s

from collections import Counter


def most_common_character(input_str):
    input_str = input_str.lower()
    new_string = "".join(input_str.split())
    result = Counter(new_string)
    result = max(result, key=result.get)
    return result

print(most_common_character('mississippis'))

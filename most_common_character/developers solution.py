# Write a function that takes in an string and returns an the most frequent char.
# The string can be a whole sentence and should ignore the chars that aren't a letter or digit.
# Sample input: mississippis
# Sample output: s

def most_common_character(input_str):
    input_str = input_str.lower()
    new_string = "".join(input_str.split())
    higher_count = 0
    return_character = ""

    for i in range(0, len(new_string)):
        count = 0
        length = len(new_string)
        j = 0
        character = new_string[i]
        while length > 0:
            if (character == new_string[j]):
                count += 1
            j += 1
            length -= 1
            if (higher_count <= count):
                higher_count = count
                return_character = character
    return (return_character)

print(most_common_character('mississippis'))

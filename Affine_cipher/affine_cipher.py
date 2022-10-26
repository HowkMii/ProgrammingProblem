# create a dictionary of the alphabets according to their corresponding numbers
alpha_dict = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25,
}

# Input the key values
key1 = int(input("Enter key1: "))
key2 = int(input("Enter key2: "))

# Input the plain text
plain_text = input("Enter plain text: ").lower()

# Initialise the cipher text
cipher_text = ""

# Convert the plain text to cipher text
for i in plain_text:
    if i.isalpha():
        cipher_text += chr(((key1 * alpha_dict.get(i)) + key2) % 26 + 97)
    else:
        cipher_text += i

# Print the cipher text
print("Cipher text: ", cipher_text)

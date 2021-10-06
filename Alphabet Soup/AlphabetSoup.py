# Given a string of alphabetical characters following the rules seen down below in part A and part B return a new string with the characters in the alphabetical order.
# Capital letters should appear before the same lowercase letter(s) in part B (Ex. aBbbCcdEe..).
#  There will be no spaces in any of the strings. Part A.)
# The string contains only lowercase letters Part B.) The string contains both lowercase and uppercase letters
#  Sample Input/Output:
#  A.) Input: "hello" Output: "ehllo"
#  B.) Input: "eLEPhAnt Output: "AEehLnPt" 


def alphabetSoup (string):
    liiiii = sorted(list(string))
    lowerLi = sorted(list(string.lower()))
    caps = []
    newString = ''
    for char in liiiii:
        if char.isupper():
            caps.append(char)
    for letter in lowerLi:
        if caps.count(letter.upper()) != 0:
            newString += letter.upper()
            caps.pop(caps.index(letter.upper()))
        else:
            newString += letter
    return newString
word = input('Enter a String: ')
print(alphabetSoup(word))

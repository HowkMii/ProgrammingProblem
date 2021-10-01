# Given a string s, find the length of the longest substring without repeating characters

# SOLUTION
# We will use the sliding window approach to solve this problem
# Basically we will "slide" through the string, pushing characters into the set until we find a repeated character
# When we find a repeated character we will drop the first element of the set
# Everytime we push a new character, we calculate if the maxLength we have is greater than the length of the set

def lengthOfLongestSubstring(s):
    lengthOfString = len(s)
    if lengthOfString == 0:
        return 0
    startIndex = 0
    endIndex = 0
    maxLength = 0
    uniqueChars = set()
    while endIndex < lengthOfString:
        if s[endIndex] not in uniqueChars:
            uniqueChars.add(s[endIndex])
            endIndex += 1
            maxLength = max(maxLength, len(uniqueChars))
        else:
            uniqueChars.remove(s[startIndex])
            startIndex += 1
    return maxLength


# Example 1
# input = abdefbasdf
# output = 6
print(lengthOfLongestSubstring("abdefbasdf"))
# Example 2
# input = aaaahhhh
# output = 2
print(lengthOfLongestSubstring("aaaahhhh"))
# Example 3
# input = *empty string*
# output = 0
print(lengthOfLongestSubstring(""))
# Example 4
# input = python
# output = 6
print(lengthOfLongestSubstring("python"))

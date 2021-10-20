# write a function that takes a string and swaps all it's uppercase letters to lowercase and it's lowercase letters to uppercase.
# digits, symbols, or whitespace should remain unchanged
# Sample input: Hello World
# Sample Output: hELLO wORLD

import string

#uc = "QWERTYUIOPASDFGHJKLZXCVBNM"
uc = string.ascii_uppercase
#lc = "qwertyuiopasdfghjklzxcvbnm"
lc = string.ascii_lowercase


def swap_case(s):
    mod = []
    for char in s:
        if char in uc:
            mod.append(lc[uc.index(char)])
        elif char in lc:
            mod.append(uc[lc.index(char)])
        elif char not in lc or char not in uc:
            mod.append(char)
            
    return "".join(mod)
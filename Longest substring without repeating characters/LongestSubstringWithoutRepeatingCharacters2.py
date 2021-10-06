def norepeats(string):
    maxcount = 1
    currentcount = 1
    seen = {string[0]:1}
    for character in string[1:]:
        if character not in seen:
            seen[character] = 1
            currentcount += 1
            continue
        if currentcount > maxcount:
            maxcount = currentcount
        currentcount = 1
        seen = {}
        seen[character] = 1
    return maxcount


# Test Cases
test1 = norepeats("ababa")      # Desired result: 2
test2 = norepeats("aaaaa")      # Desired result: 1
test3 = norepeats("abcdabcd")   # Desired result: 4

if (test1 == 2) and (test2 == 1) and (test3 == 4):
    print("All tests Passed")
else:
    print(">= 1 test failed")

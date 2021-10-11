from capital_indexes import capital_indexes

tests = [
    "HeLlO WorlD!",
    "my CaPs LoCk KeY iS bRoKen!",
    "HapPy HacKToBeRFeSt!",
]

for index, item in enumerate(tests):
    print(f'Test {index+1}: {item}\nOutput: {capital_indexes(item)}\n')
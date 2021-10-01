# List of multiples.
three = []
five = []

# List of numbers
numbers = []

# Get multiples and numbers.
for n in range(100):
    three.append((n + 1) * 3)
    five.append((n + 1) * 5)
    numbers.append(n + 1)

# Magic(TM)
for m in numbers:
    if m in three and not m in five:
        print("fizz")
    elif m in five and not m in three:
        print("buzz")
    elif m in three and m in five:
        print("fizzbuzz")
    else:
        print(m)

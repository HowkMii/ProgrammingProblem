'''
Q. What is Ugly Number ?
Ans: Ugly numbers are numbers whose only prime factors are 2, 3 or 5. 
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … 
shows the first 11 ugly numbers. 
By convention, 1 is included.
'''

def ugly_numbers(n: int) -> int:        # Function starts here ...
    ugly_nums = [1]
    i2, i3, i5 = 0, 0, 0
    next_2 = ugly_nums[i2] * 2
    next_3 = ugly_nums[i3] * 3
    next_5 = ugly_nums[i5] * 5

    for _ in range(1, n):
        next_num = min(next_2, next_3, next_5)
        ugly_nums.append(next_num)
        if next_num == next_2:
            i2 += 1
            next_2 = ugly_nums[i2] * 2
        if next_num == next_3:
            i3 += 1
            next_3 = ugly_nums[i3] * 3
        if next_num == next_5:
            i5 += 1
            next_5 = ugly_nums[i5] * 5
    return ugly_nums[-1]                # ... Function ends here.

'''
          ---::Output::---
Returns the nth ugly number.
>>> ugly_numbers(100)
1536
>>> ugly_numbers(0)
1
>>> ugly_numbers(20)
36
>>> ugly_numbers(-5)
1
>>> ugly_numbers(-5.5)
Traceback (most recent call last):
    ...
TypeError: 'float' object cannot be interpreted as an integer
'''

if __name__ == "__main__":              # Mock testing with a sample value
    from doctest import testmod
    testmod(verbose=True)
    print(f"{ugly_numbers(200) = }")

"""
Q. What is an Armstrong number ?
Ans: An Armstrong number is a number which is equal to the sum of its own digits each raised to the
power of the number of digits.

Ex: 370 is an Armstrong number because 3*3*3 + 7*7*7 + 0*0*0 = 370.
"""

def armstrong_number(n: int) -> bool:           # Function starts here ...
    
    if not isinstance(n, int) or n < 1:
        return False

    # Initialization of sum and number of digits.
    total = 0
    number_of_digits = 0
    temp = n
    # Calculation of digits of the number
    while temp > 0:
        number_of_digits += 1
        temp //= 10
    # Dividing the number into separate digits and find Armstrong number
    temp = n
    while temp > 0:
        rem = temp % 10
        total += rem**number_of_digits
        temp //= 10
    return n == total                           # ... Function ends here

# the main function to take inputs and give outputs
def main():
    num = int(input("Enter an integer to see if it is an Armstrong number: ").strip())
    print(f"{num} is {'' if armstrong_number(num) else 'not '}an Armstrong number.")
    
"""                   ---::Output::---
>>> Enter an integer to see if it is an Armstrong number: 7
7 is an Armstrong number.

>>> Enter an integer to see if it is an Armstrong number: 1634
1634 is an Armstrong number.

>>> Enter an integer to see if it is an Armstrong number: 10
10 is not an Armstrong number.
"""

if __name__ == "__main__":        # Mock testing
    import doctest

    doctest.testmod()
    main()

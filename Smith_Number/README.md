Create a Python programs to check if the given number is smith or not. The smith number program frequently asked in Java coding tests and academics.

A Smith number is a composite number whose sum of digits equals to the sum of digits of its prime factors, excluding 1. It is also known as a joke number. It is a sequence of OEIS A006753.
Sum of digits of n = Sum of digits of prime factors of n (counted with multiplicity)

Let's understand it through an example.

Smith Number Example

Example 1: Suppose, we want to check the number 85 is smith or not.
Sum of digits = 8 + 5 = 13
Prime factors of 85 is: 5,17
Sum of digits of its prime factors = 5 + 1+ 7 = 13
Compare the sum of digits with the sum of digits of its prime factors i.e. 13=13. Both are equal. Hence, the given number (85) is a smith number.

Example 2: Let's check another number 999 is smith or not.
Sum of digits = 9+ 9+9 = 27
Prime factors of 999 is: 3×3×3,37
Sum of digits of its prime factors = 3+3+3+3+7 =19
Compare the sum of digits with the sum of digits of its prime factors i.e. 27≠19. Hence, the given number (999) is not a smith number.



Similarly, we can check other numbers also. Some other smith numbers are 4, 27, 85, 94, 121, 166, 202, 265, 274, 319, 346, 666, etc.

Steps to Find Smith Number

Read or initialize a number from the user.

Find the sum of its digits.

Find the prime factors of the given number.

Determine the sum of digits of its prime factors.

Compare the sum of digits with the sum of digits of its prime factors.

If they are equal, the given number is a smith

Else, not a smith number.

"""
Q. What is an Armstrong number ?
Ans: An Armstrong number is a number which is equal to the sum of its own digits each raised to the
power of the number of digits.
Ex: 370 is an Armstrong number because 3*3*3 + 7*7*7 + 0*0*0 = 370.
"""
def armstrong_number_series(lower,upper):               # function starts here ...
    arm_nums = []
    for num in range(lower,upper + 1):
      # Initialization of sum and number of digits.
      total = 0
      number_of_digits = 0    
      temp = num
      # Initialization of sum and number of digits.  
      while temp > 0:  
          number_of_digits += 1
          temp //= 10
      # Dividing number into separate digits and find Armstrong number 
      temp = num
      while temp > 0:
          rem = temp % 10
          total += rem**number_of_digits
          temp //= 10 
      if num == total:
          arm_nums.append(num)
    return arm_nums                                     # ... function ends here
                
"""                   ---::Output::---
>>> Enter lower range: 1
>>> Enter upper range: 500
[1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
>>> Enter lower range: 240
>>> Enter upper range: 10000
[370, 371, 407, 1634, 8208, 9474]
"""

# Input Output section of the code
lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))
print(armstrong_number_series(lower,upper))

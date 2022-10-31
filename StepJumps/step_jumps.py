# https://www.codechef.com/submit/XJUMP

# For the following input:
# 4
# 4 2
# 8 3
# 3 4
# 2 1
#
#The output should be:
# 2
# 4
# 3
# 2

import sys

inputs = input().split()
if len(inputs) != 2:
    sys.exit()

x_target_step, y_steps = tuple([int(i) for i in inputs])
if x_target_step % y_steps == 0:
    print(int(x_target_step / y_steps))
else:
    full_steps = int(x_target_step / y_steps)
    remaining = x_target_step - (full_steps * y_steps)
    print(full_steps + remaining)

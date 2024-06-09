import random

print(random.randint(5, 20))  # line 1
# The output is like(6,7,19,8, etc.)
# The smallest number is 5, the largest is 20.

print(random.randrange(3, 10, 2))  # line 2
# The output is like (3, 5, 9, etc.)
# The smallest number is 3,and the largest is 9
# No, because the step is 2, so it only generates odd numbers between 3 and 10

print(random.uniform(2.5, 5.5))  # line 3)
# because the step is 2, so it only generates odd numbers between 3 and 10
# The output is like 3.67, 4.21, 5.12, etc.)
# Answer: The smallest number is 2.5, the largest is 5.5.

print(random.randint(1,100))
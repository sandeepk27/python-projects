
# It imports the random module

import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$"
special = "*%&^"

# It creates a string of all the characters that can be used in the password.
total = lower + upper + numbers + symbols + speical

len = 12
# It creates a random password.
password = "".join(random.sample(total, len))
print(password)


# Grouping the tuples by the second element in the tuple.
t = [(2, 1), (1, 1), (2, 4), (2, 6), (7, 5), (6, 4)]
result = {}
for i, j in t:
    result.setdefault(j, []).append(i)
print(result)

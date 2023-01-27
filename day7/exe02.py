import time
import random

random_number = []

for x in range(100):
    n = random.randint(1, 1000)
    random_number.append(n)

for b in random_number:
    time.sleep(1)
    print(b, end=" ")

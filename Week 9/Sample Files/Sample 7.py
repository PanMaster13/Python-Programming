#Sample7.py

import random
def randomLine(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

print(randomLine("write.txt"))

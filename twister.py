from itertools import product
from random import randint

colors = ["blue", "green", "yellow", "red"]
sides = ["right", "left"]
appendages = ["hand", "foot"]
options = [sides, appendages, colors]
options = [' '.join(i) for i in product(*options)]

while True:
    opt_ind = randint(0, len(options)-1)
    print('{}: {}'.format(opt_ind, options[opt_ind]), end='')
    input()

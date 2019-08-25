from itertools import product

colors = ["blue", "green", "yellow", "red"]
limbs = [''.join(i) for i in product(["right", "left"], ["hand", "foot"])]

print(colors)
print(limbs)

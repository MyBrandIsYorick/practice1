import itertools
from itertools import permutations

li = input().split()

for i in itertools.permutations(li):
    print(i)

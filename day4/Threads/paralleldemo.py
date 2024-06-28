import multiprocessing as multip
print("Total number of processors on your machine is: ", multip.cpu_count())

import numpy as nump
from time import time
#RandomState from numpy is used for the vast number of
#  probability distributions in selection.
nump.random.RandomState(110)
#random.randint(a,b) will return a pseudorandom integer between a and b.
met = nump.random.randint(0, 11, size=[300000, 6])
#print(met)
collect = met.tolist()

#print(collect)

def total_range(row, min, max):

    total = 0
    for x in row:
        if min <= x <= max:
         total = total + 1
    return total


def total_range_row(row, min=5, max=8):
    total = 0
    for x in row:
          if min <= x <= max:
              total = total + 1
    return total

outcome = []
for row in collect:
    outcome.append(total_range( row, min=4, max= 8))
#print(outcome[:10])


import multiprocessing as multip
if __name__ == '__main__':
    poolv = multip.Pool(multip.cpu_count())
    outcomes = [poolv.apply(total_range, args=(row, 5,9)) for row in collect]
    poolv.close()
    print(outcomes[:10])
    poolv = multip.Pool(multip.cpu_count())
    outcomes = poolv.map(total_range_row, [row for row in collect])
    poolv.close()
    print(outcomes[:10])
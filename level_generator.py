#!/usr/bin/python3

import os
import random
DEPTH = 4

level_num = len(os.listdir("levels")) + 1


n = int(input("Insert number of cones: "))

ll = []
for i in range(1, n + 1):
    ll.extend([i for d in range(DEPTH)])

random.shuffle(ll)

fout = open(f"levels/{level_num}.cones", 'w')
print(n, 2, file=fout)
for i in range(n):
    print(*ll[i * 4: (i + 1) * 4], file=fout)

fout.close()

print(f"Level saved to levels/{level_num}.cones")
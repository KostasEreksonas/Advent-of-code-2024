#!/usr/bin/env python3

with open("test") as f:
    c1, c2 = [[] for x in range(2)]
    for l in f:
        x = l.split()
        c1.append(x[0])
        c2.append(x[1])

t = 0
for i in c1:
    s = 0
    for j in c2:
        if (i == j):
            s += 1
    t += s*int(i)
    print(f"{i}: {s}, {t}")

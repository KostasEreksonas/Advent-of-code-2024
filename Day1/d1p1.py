#!/usr/bin/env python3

with open("test") as f:
    t = 0
    c1, c2 = [[] for x in range(2)]
    for l in f:
        x = l.split()
        c1.append(x[0])
        c2.append(x[1])
    c1.sort()
    c2.sort()
    for x in range(0, len(c1)):
        r = int(c1[x]) - int(c2[x])
        if (r < 0):
            r = -1 * r
        t += r
        print(f"{c1[x]}, {c2[x]}, {r}, {t}")

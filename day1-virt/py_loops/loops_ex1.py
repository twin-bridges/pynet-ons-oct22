#!/usr/bin/env python

# Range technically builds an iterable and not a list
for i in range(1, 50):
    if i == 13:
        continue
    print(i)
    if i == 39:
        break

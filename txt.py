#!/usr/bin/env python3
import os

some_word = ('Jobs said:').strip()
keep = ""
for line in open('Jobs.txt'):
    for i in line.split(some_word):
        keep = keep + ''.join(str(i))
print(keep)

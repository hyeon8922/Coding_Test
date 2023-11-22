# -*- coding: utf-8 -*-
import sys

n, k = map(int, sys.stdin.readline().split())

t = input()

for i in t:
    print(i*k, end='')

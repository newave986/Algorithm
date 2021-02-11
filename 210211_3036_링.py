# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 22:19:16 2021

@author: newave986.git
"""

# BOJ # 3036 링
# https://www.acmicpc.net/problem/3036

import sys

N = int(sys.stdin.readline())
ring = list(map(int, sys.stdin.readline().split()))
main = ring[0]
ring.remove(ring[0])


def GCD(x, y):
    
    value = 1
    
    a = min(x, y)
    b = max(x, y)

    for k in range (2, a+1):
        if a % k == 0 and b % k == 0:
            value = k
    
    return value


for i in range(len(ring)):
    
    # print(main/ring[i])
    # 기약분수 형태로 표현하는 것이 문제
    
    value = GCD(main, ring[i])
    print(str(int(main/value)) + "/" + str(int(ring[i]/value)))
    
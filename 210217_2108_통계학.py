# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 13:19:06 2021
Changed on Thu Feb 18 14:08:55 2021

@author: newave986.git 
"""

# https://www.acmicpc.net/problem/2108

# BOJ 2108 통계학 - 정렬

from math import ceil
import sys

def round_number(numlist, n): # 1. 산술평균 구하는 함수 round_number
    x = sum(numlist) / n
    
    if x - 0.5 % 1 == 0:
        return int(ceil(x))
    
    return int(round(x, 0))
    
def mid_number(numlist, n): # 중앙값 구하는 함수 mid_number
    return numlist[n//2]

    
def most_number(numlist, n): # 최빈값 구하는 함수 most_number
    
    t = - numlist[0]
    mostnumlist = [numlist[i] + t for i in range(n)]
    
    count = [0 for _ in range(max(mostnumlist) + 1)]
    c = []
                
    for k in range(n):
        count[mostnumlist[k]] += 1
            
    count_max = max(count)

    for j in range(len(count)):
        if count[j] == count_max:
            c.append(j)
    
    if len(c) == 1:
        return c[0] - t
    else:
        return c[1] - t
    
    
def range_number(numlist, n): # 범위 구하는 함수 range_number
    return numlist[n-1] - numlist[0]


n = int(sys.stdin.readline())
numlist = []

for i in range(n):
    num = int(sys.stdin.readline())
    numlist.append(num)

numlist.sort()

print(round_number(numlist, n))
print(mid_number(numlist, n))
print(most_number(numlist, n))
print(range_number(numlist, n))


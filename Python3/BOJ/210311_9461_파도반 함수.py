# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 12:31:02 2021

@author: newave986.git
"""

# BOJ #9461
# https://www.acmicpc.net/problem/9461
# 파도반 수열

"""
기본 다이나믹 프로그래밍 이용
피보나치 함수의 다이나믹 프로그램과 정확하게 동일한 원리
"""

# import sys
# input = sys.stdin.readline()

def padovan(x):
    global visit
    if x == 1 or x == 2 or x == 3:
        return 1
    if visit[x] != 0:
        return visit[x]
    visit[x] = padovan(x-2) + padovan(x-3)
    return visit[x]
    
T = int(input())
for _ in range(T):
    N = int(input())
    visit = [0] * (N + 1)
    print(padovan(N))
    
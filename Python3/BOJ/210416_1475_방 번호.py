# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 03:55:24 2021

@author: newave986.git
"""

# BOJ 1475 구현 방 번호
# https://www.acmicpc.net/problem/1475

import sys
import math

input = sys.stdin.readline

def roomNumCount(n):
    roomNum = list(map(int, str(n)))
    roomList = [0 for _ in range(10)]
    
    roomNum.sort()
    for i in range(0, 10):
        roomList[i] = roomNum.count(i)

    k = math.ceil((roomList[6] + roomList[9]) / 2)
    roomList[6] = k
    roomList[9] = k
    
    return max(roomList)
    
n = int(input())
print(roomNumCount(n))
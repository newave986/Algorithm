# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 23:26:07 2021

@author: newave986.git
"""

# BOJ 10816 https://www.acmicpc.net/problem/10816
# 숫자 카드 2
# Binary Search
#

import sys
input = sys.stdin.readline

def binarySearch(start, end, x):
    
    global card
    global count
    
    if start > end:
        return 0
    
    mid = (start + end) // 2
    
    if x < card[mid]:
        binarySearch(start, mid - 1, x)
        
    elif x > card[mid]:
        binarySearch(mid + 1, end, x)
    
    if x == card[mid]:
        del card[mid]
        count += 1
        return 1
        
    
N = int(input())
card = list(map(int, input().split()))
card.sort()

M = int(input())
get = list(map(int, input().split()))


for i in get:
    
    count = 0
    
    while binarySearch(0, len(card)-1, i) == 1:
        binarySearch(0, len(card)-1, i)
        
    print(count, end = ' ')
    
    
    
    
    
    
    
    
    
    
    
    
    

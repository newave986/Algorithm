# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:36:03 2021

@author: newave986.git
"""

# https://www.acmicpc.net/problem/18258
# #18258 큐2

import sys

from collections import deque

queue = deque()
status = 0

def push(x):
    global deque
    global status
    status += 1
    queue.append(x)
    
def pop():
    global deque
    global status
    if status == 0:
        return '-1'
    else:
        status -= 1
        return queue.popleft()

def size():
    global deque
    global status
    return status

def empty():
    global deque
    global status
    if status == 0:
        return '1'
    else:
        return '0'
    
def front():
    global deque
    global status
    if status == 0:
        return '-1'
    else:
        return queue[0]

def back():
    global deque
    global status
    if status == 0:
        return '-1'
    else:
        return queue[status-1]
    


N = int(sys.stdin.readline())

for _ in range(N):
    
    do = list(sys.stdin.readline().split())
    
    if do[0] == 'push': 
        push(int(do[1]))
    elif do[0] == 'pop': print(pop())
    elif do[0] == 'size': print(size())
    elif do[0] =='empty': print(empty())
    elif do[0] == 'front': print(front())
    elif do[0] == 'back': print(back())
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 04:18:43 2021

@author: newave986.git
"""

# BOJ #11725 트리 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725

# import sys
# input = sys.stdin.readline

def makeNode():
    global node
    for _ in range(N):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)

def findParent(node):
    global layer
    layer[0] = node[0]
    for i in node[0]:
        visit[i] = 1
        layer[1].append(node[i])
    
    

N = int(input())
node = [[0] for _ in range(N)]
visit = [0 for _ in range(N)]
layer = []

makeNode()


    
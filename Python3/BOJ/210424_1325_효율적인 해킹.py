# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 17:26:39 2021

@author: newave986.git
"""

# BOJ #1325 효율적인 해킹
# https://www.acmicpc.net/problem/1325
# BFS 연습

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
trust = [[] for _ in range(N + 1)]
connect = [[] for _ in range(N + 1)]

# 신뢰 관계를 입력받는다.
for _ in range(M):
    a, b = map(int, input().split())
    # a가 b를 신뢰하므로, b를 해킹하면 a를 해킹할 수 있다는 뜻이다.
    # 따라서 a와 b를 입력받았을 때 나는 graph[b]에만 a를 추가해 준다.
    # graph[a]에는 b를 추가하지 않음을 유의한다.
    trust[b].append(a)
    # 대신 연결되어 있음을 알려 주기 위해 connect list를 선언한다.
    connect[a].append(b)

# 신뢰 관계를 bfs에 따라 구한다.
# 신뢰 관계 덩어리를 만들기 위해 bfs를 사용한다.

visit = [0 for _ in range(N + 1)]
countList = [[], []]

queue = []
queue = deque(queue)
maximum = 0

def bfs(trust, start):

    comList = [start]
    
    global countList 
    global visit
    global queue
    global maximum

    visit[start] = 1
    queue.append(start)
    
    while queue:
        v = queue.popleft()
        
        for i in trust[v]:
            
            if visit[i] != 1:
                visit[i] = 1
                comList.append(i)
                queue.append(i)
            
        for j in connect[v]:

            if visit[j] != 1:
                if v in trust[j]:
                    visit[v] = 2
                    break
                
    if visit[start] != 2:
            if len(comList) >= maximum:
                maximum = len(comList)
                countList[0].append(maximum)
                countList[1].append(start)
                
    
# 아직 방문하지 않은 노드에 대하여 bfs로 신뢰 관계 덩어리를 만든다.
bfs(trust, 1)

while True:
    k = [i for i, value in enumerate(visit) if value == 0]
    if len(k) == 1:
        break
    bfs(trust, k[1])

# 신뢰 관계 덩어리의 head 컴퓨터 번호를 오름차순으로 출력한다.

for p in range(len(countList[0])):
    if countList[0][p] == maximum:
        print(countList[1][p], end=" ")

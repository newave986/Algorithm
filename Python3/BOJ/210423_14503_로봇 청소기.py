# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 11:51:04 2021

@author: newave986.git
"""

# BOJ #14503 로봇 청소기
# DFS 이용
# https://www.acmicpc.net/problem/14503

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())

graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))
    
cleanBlock = 1
graph[r][c] = 2

# DFS로 구현

def dfs(start, d):
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    global graph
    global cleanBlock
    
    d = (d-1) % 4

    x = int(start[0])
    y = int(start[1])
    
    if (x + dx[d] < 0 or x + dx[d] >=N or y + dy[d] < 0 or y + dy[d] >= M):
        pass
    
    else:
        
        if graph[x + dx[d]][y + dy[d]] == 0:
            cleanBlock += 1
            graph[x + dx[d]][y + dy[d]] = 2
            dfs((x + dx[d], y + dy[d]), d)
                
        else:
            
            status = 1
        
            for t in range(1, 4):
                
                tmp_d = (d - t) % 4
                
                tmp_x = x + dx[tmp_d]
                tmp_y = y + dy[tmp_d]
                
                if (tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= M):
                    pass
                    
                elif graph[tmp_x][tmp_y] == 0:
                    cleanBlock += 1
                    graph[tmp_x][tmp_y] = 2
                    dfs((tmp_x, tmp_y), tmp_d)
                    status = 0
                    break
        
            if status == 1:
                
                if (x - dx[(d+1)%4] < 0 or x - dx[(d+1)%4] >= N or y - dy[(d+1)%4] < 0 or y - dy[(d+1)%4] >= M):
                    pass
                                
                elif graph[x - dx[(d+1)%4]][y - dy[(d+1)%4]] == 2:
                        dfs((x- dx[(d+1)%4], y - dy[(d+1)%4]), (d+1)%4)
                        
                else: return
                    
                    
                        
dfs((r, c), d)
print(cleanBlock)

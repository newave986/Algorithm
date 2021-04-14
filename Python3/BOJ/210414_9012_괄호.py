# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 17:30:05 2021

@author: newave986.git
"""

# BOJ 9012 괄호
# https://www.acmicpc.net/problem/9012

n = int(input())

def VPS(k):
    s = []
    
    for i in k:
        if i == "(":
            s.append(i)
        else:
            if len(s) == 0:
                return False
            else: s.pop()
            
    if len(s) == 0: return True
    else: return False
  
def parenthesis(k):
    if (VPS(k)): print("YES")
    else: print("NO")
    
for _ in range(n):
    k = list(input())
    parenthesis(k)
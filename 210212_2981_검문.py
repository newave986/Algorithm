# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 20:33:32 2021

@author: newave986.git
"""


import sys
# sys.stdin.readline()

num_list = []
m_list = []

N = int(input())
for _ in range(N):
    num_list.append(int(input()))
num_list.sort()

def GCD(x, y):
    
    value = []

    for k in range (2, x+1):
        if x % k == 0 and y % k == 0:
            value.append(k)
            
    return value


def Mcount(array):   
    
    tmp = []
    for i in range(len(num_list)-1):
        tmp.append(num_list[i+1] - num_list[i])   
    
    global m_list  
    global N
    
    if N == 2:
        if num_list[1] % num_list[0] == 0:
            status = num_list[0]
        else:
            status = num_list[1] - num_list[0]
              
        for i in range(1, int(status ** (1/2)) + 1):
            if status % i == 0:
                m_list.append(int(i))
                m_list.append(int(status/i))
        m_list.remove(1)
            

    else:
        k = GCD(tmp[0], tmp[1])
        for M in k:
            status = 0     
            for j in tmp:
                if j % M != 0:
                    status = 1    
                if status== 1:
                    break
            if status == 0:
                m_list.append(M)
            

    m_list.sort()

    
Mcount(num_list)

for i in m_list:
    print(i, end =" ")
    
    
    
    
    
    
    
    
# 2020 카카오 인턴십 - 수식 최대화

import copy

def splitNum(arr, expression):
    expression = list(expression)
    tmp = []
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for e in range(len(expression)):
        if expression[e] in number:
            tmp.append(expression[e])
        if expression[e] not in number:
            tmp = "".join(tmp)
            arr.append(int(tmp))
            arr.append(expression[e])
            tmp = []
        if e == len(expression) - 1:
            tmp = "".join(tmp)
            arr.append(int(tmp))
    return arr

def plusCalculate(new):
    plusIndex = list(filter(lambda x: new[x] == "+", range(len(new))))
    if len(plusIndex) != 0:
        for i in range(len(plusIndex)):
            k = plusIndex[i] - 2*i
            new[k] = new[k-1] + new[k+1]
            new[k-1] = "@"
            new[k+1] = "@"
            new.remove("@")
            new.remove("@")
    return new

def minusCalculate(new):
    minusIndex = list(filter(lambda x: new[x] == "-", range(len(new))))
    if len(minusIndex) != 0:
        for i in range(len(minusIndex)):
            k = minusIndex[i] - 2*i
            new[k] = new[k-1] - new[k+1]
            new[k-1] = "@"
            new[k+1] = "@"
            new.remove("@")
            new.remove("@")
    return new

def multipleCalculate(new):
    multipleIndex = list(filter(lambda x: new[x] == "*", range(len(new))))
    if len(multipleIndex) != 0:
        for i in range(len(multipleIndex)):
            k = multipleIndex[i] - 2*i
            new[k] = new[k-1] * new[k+1]
            new[k-1] = "@"
            new[k+1] = "@"
            new.remove("@")
            new.remove("@")
    return new

def getMax(arr, score):
    score.append(arr[0])

    new1 = copy.deepcopy(arr)
    score.append(abs(pMiMu(new1)))

    new2 = copy.deepcopy(arr)
    score.append(abs(pMuMi(new2)))

    new3 = copy.deepcopy(arr)
    score.append(abs(miPMu(new3)))

    new4 = copy.deepcopy(arr)
    score.append(abs(miMuP(new4)))

    new5 = copy.deepcopy(arr)
    score.append(abs(muPMi(new5)))

    new6 = copy.deepcopy(arr)
    score.append(abs(muMiP(new6)))

    return score

# 최대 3! = 6개의 연산 정의
def pMiMu(arr):
    arr = plusCalculate(arr)
    arr = minusCalculate(arr)
    arr = multipleCalculate(arr)
    return arr[0]

def pMuMi(arr):
    arr = plusCalculate(arr)
    arr = multipleCalculate(arr)
    arr = minusCalculate(arr)
    return arr[0]

def muPMi(arr):
    arr = multipleCalculate(arr)
    arr = plusCalculate(arr)
    arr = minusCalculate(arr)
    return arr[0]

def muMiP(arr):
    arr = multipleCalculate(arr)
    arr = minusCalculate(arr)
    arr = plusCalculate(arr)
    return arr[0]

def miPMu(arr):
    arr = minusCalculate(arr)
    arr = plusCalculate(arr)
    arr = multipleCalculate(arr)
    return arr[0]

def miMuP(arr):
    arr = minusCalculate(arr)
    arr = multipleCalculate(arr)
    arr = plusCalculate(arr)
    return arr[0]

def solution(expression):
    arr = []
    score = []

    arr = splitNum(arr, expression)
    score = getMax(arr, score)

    answer = max(score)
    return answer
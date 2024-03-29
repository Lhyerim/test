# 문제 3번 #

def plus(v1, v2, v3 = 0):
    result = 0
    result = v1 + v2 + v3
    return result

hap = plus(100, 200, 300)
print(hap)

# 답 1: v1, v2, v3 = 0 ; 답 2: return result

print("------------------------------")

# 문제 4번 #

def f1():
    print(var)

def f2():
    var = 10
    print(var)

var = 100

f1()
f2()

# 답: 100, 10

print("------------------------------")

# 문제 11 #

def addNumber(num):
    if num <= 1 :
        return 1
    return num+addNumber(num-1)

print(addNumber(100))

# 답: if num <= 1:
#          return 1
#     return num+addNumber(num-1)

print("------------------------------")

# 문제 8 #

def myFunc(p1 = 1, p2 = 2, p3 = 3):
    ret = p1 + p2 + p3
    return ret

print("매개변수 없이 호출 ==> ", myFunc())
print("매개변수가 1개로 호출 ==> ", myFunc(1))
print("매개변수가 2개로 호출 ==> ", myFunc(1, 2))
print("매개변수가 3개로 호출 ==> ", myFunc(1, 2, 3))

# 답: p1 = 1, p2 = 2, p3 = 3


# 문제 5번 #

ss = 'Python'

for i in range(0, len(ss)):
    print(ss[i] + '$', end="")

# 답 1: for, 2: len(ss), 3: ss[i]
print("")
print("----------------------------------")

# 문제 11번 #

import re

string = '파이썬343CookBook@@@열공중%^&%'
result = re.sub(r'[^A-Za-z가-힣]+', '', string)
print(result)

print("----------------------------------")

# 문제 9번 #

inStr, outStr = "Python", ""
strLen = len(inStr)

for i in range(0, strLen):
    outStr += inStr[strLen - (i+1)]

print("내용을 거꾸로 출력 --> %s" % outStr)

# 답: inStr[strLen - (i+1)]

print("----------------------------------")

# 심화문제 13 #

import turtle
import random
from tkinter.simpledialog import *
import math

## 전역 변수 선언 부분 ##

inStr = ""
swidth, sheight = 500, 500
radius, angle = 200, 0
txtSize = 20

## 메인 코드 부분 ##

turtle.title('거북이 글자쓰기')
turtle.shape('turtle')
turtle.setup(width=swidth + 50, height=sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()

inStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')
angle_step = (360 * 2) / len(inStr)  # 문자열의 길이로 회전 각도 설정

for ch in inStr:
    radian = math.radians(angle)
    tX = radius * math.cos(radian)
    tY = radius * math.sin(radian)
    r = random.random()
    g = random.random()
    b = random.random()

    turtle.goto(tX, tY)

    turtle.pencolor((r, g, b))
    turtle.write(ch, font=('맑은 고딕', txtSize, 'bold'))

    radius -= 3 

    angle += angle_step  # 각도를 증가시켜 나선형으로 회전

turtle.done()


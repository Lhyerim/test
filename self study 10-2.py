from tkinter import *
import random

## 전역 변수 선언 부분 ##
btnList = [None]*9
fnameList = ["honeycomb.gif", "icecream.gif", "jellybean.gif", "kitkat.gif",
             "lollipop.gif", "marshmallow.gif", "nougat.gif", "oreo.gif", "pie.gif"]
photoList = [None]*9
i,k = 0, 0
xPos, yPos = 0, 0
num = 0

## 메인 코드 부분 ##
window = Tk()
window.geometry("600x600")

## shuffle 함수 사용 ##
random.shuffle(fnameList)

for i in range(0,9):
    photoList[i] = PhotoImage(file = "gif/" +fnameList[i])
    btnList[i] = Button(window, image=photoList[i])

for i in range(0,3):
    for k in range(0,3):
        btnList[num].place(x=xPos, y=yPos)
        num += 1
        xPos += 200
    xPos = 0
    yPos += 200

window.mainloop()

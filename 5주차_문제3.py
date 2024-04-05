## 문제 5번 ##

from tkinter import *
from time import *

fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif",
             "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]

num = 0

def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    pLabel.configure(text=fnameList[num])

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    pLabel.configure(text=fnameList[num])

def initialize_label():
    pLabel.configure(text=fnameList[num])
    
window = Tk()
window.geometry("500x200")
window.title("사진 앨범 보기")


btnPrev = Button(window, text="<< 이전", command = clickPrev)
btnNext = Button(window, text="다음 >>", command = clickNext)

pLabel = Label(window)

btnPrev.place(x=100, y=100)
btnNext.place(x=350, y=100)
pLabel.place(x=220, y=100)

initialize_label()

window.mainloop()

from tkinter import *
from tkinter.filedialog import *

## 함수 선언 부분 ##
def func_open() :
    filename = askopenfilename(parent=window, filetypes=(("GIF 파일", "*.gif"),
                                                         ("모든 파일","*.*")))
    photo = PhotoImage(file = filename)

# 이미지 픽셀 크기
    width = photo.width()
    height = photo.height()

    for x in range(width):
        for y in range(height):
            # RGB 값
            red, green, blue = photo.get(x, y)
            # 회색 값
            gray = int((red+green+blue)/3)
            # 픽셀 값 회색으로 변환
            photo.put("#%02x%02x%02x" % (gray, gray, gray), (x, y))
            
    
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit():
    window.quit()
    window.destroy()

## 메인 코드 부분 ##
window = Tk()
window.geometry("400x400")
window.title("명화 감상하기")

photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack(expand=1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)

window.mainloop()

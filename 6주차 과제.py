# 문제 1번 #

# 입력 관련 함수: input(), read(), readline(), readlines()
# 출력 관련 함수: print(), write(), writeline()

# 문제 2번 #

#순서대로: 파일 열기 -> 파일 읽기/쓰기 -> 파일 닫기
#답은 1번

# 문제 3번 #

# 1번: 생략하면 쓰기 모드가 아닌 읽기 모드가 기본으로 설정된다
# 3번: a는 쓰기 모드이지만 기존 파일을 삭제하지 않으며, 기존 파일 끝에 데이터를 추가한다
# 6번: python 파일 열기 모드에서 tb 모드는 없다.

# 문제 4번 #

inFp = None
inStr = ""

inFp = open("C:/Temp/data1.txt", "r")

inStr = inFp.readlines()
print(inStr, end="")

inFp. close()

#답 1번: open, 2번: readlines, 3번: close

#문제 6번 #

inFp = open("C:/Windows/win.ini", "r")
outFp = open("C:/Temp/data3.txt", "w")

inList = inFp.readlines()
for inStr in inList :
    print(inStr, end="")

inFp.close()
outFp.close()

#답 1번: inFp.readlines(), 2번: print(inStr, end="")

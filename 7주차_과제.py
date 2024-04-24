## 2번 문제 ##

class Car:
    color = ""
    speed = 0

    def upSpeed(self, value):
        self.speed += value

# def upSpeed에서 (self) 추가
# 따라서 아래 변수도 self.speed로 변경


## 4번 문제 ##

class Horse:
    speed = 0

    def __init__(self, speed):
        self.speed = 50

## 6번 문제 ##

class Car:
    def method(self):
        print("슈퍼 클래스")

class Sedan(Car):
    def method(self):
        print("서브 클래스")

myCar = Car()
mySedan = Sedan()
myCar.method()
mySedan.method()

# 답: 3번 슈퍼클래스 서브 클래스

## 7번 문제 ##

class Car:
    speed = 0

    def upSpeed(self, value):
        self.speed = self.speed + value

class RV(Car):
    seatNum = 0

    def getSeatNum(self):
        return self.seatNum


# 빈칸: class RV(Car):

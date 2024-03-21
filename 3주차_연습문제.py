# 연습문제 4번 #

score = int(input("점수를 입력하세요 : "))

if score >= 90 :
    print("장학생", end='')

else :
    if score >= 60 :
        print("합격", end='')

    else :
        print("불합격", end='')

print("입니다. ^^")

print("------------------------")

# 연습문제 5번 #

num = 5
if num % 2 == 0 :
    res = '짝수'
else :
    res = '홀수'
print(res)

print("------------------------")

num = 5
res = '짝수' if num % 2 == 0 else '홀수'  # 연습문제 5번 정답은 3번
print(res)

print("------------------------")

# 연습문제 6번 #

nn = [100, 200, 300, 400, 500]

nn[1] = 700
print(nn) #연습문제 6-1번 : nn = [100, 700, 300, 400, 500]

nn = [100, 200, 300, 400, 500]

nn[1] = [444, 555]
print(nn) #연습문제 6-2번 : nn = [100, [444, 555], 300, 400, 500]

nn = [100, 200, 300, 400, 500]

nn[1:4] = [444, 555]
print(nn) #연습문제 6-3번 : nn = [100, 444, 555, 500]

nn = [100, 200, 300, 400, 500]

nn[2:] = []
print(nn) #연습문제 6-4번 : nn = [100, 200]


print("------------------------")

# 연습문제 9번 #

hap2 = 0

for n in range(3333, 10000, 1):
    if n % 1234 == 0:
        hap2 += n
        continue
    if hap2 + n> 100000:
        break

print(hap2) #1234의 배수의 합계는 문제 속 출력결과와 다릅니다.
#문제 속 출력결과가 나오려면 1234의 배수가 아닌 수의 합계를 구해야합니다.


hap3 = 0

for n in range(3333, 10000, 1):
    if n % 1234 == 0:
        continue
    hap3 += n
    if hap3 + n> 100000:
        break

print(hap3) # 연습문제 속 출력결과가 나오는 1234의 배수가 아닌 수의 합계입니다.


print("------------------------")

# 연습문제 8번 #

hap = 0
for n in range(1234, 4568) :
    if n%444 == 0 :
        hap += n

print(hap)

#for문을 while문으로 변경

hap1=0
n = 1234

while n <= 4567 :
    if n % 444 == 0 :
        hap1 += n
        n += 1
    else : n += 1

print(hap1)


print("------------------------")


# 연습문제 14번 #

myData = [[n*m for n in range(1,3)]for m in range(2,4)]

print(myData)

print("------------------------")


# 연습문제 5번 #

nn = [100, 200, 300, 400, 500]

print(nn[4]) # 6-1번
print(nn[-1]) # 6-2번
print(nn[-2]) # 6-3번
print(nn[1:4]) # 6-4번
print(nn[0:1]) # 6-5번
print(nn[2:-1]) # 6-6번
print(nn[0::2]) # 6-7번
print(nn[::-1]) # 6-8번
print(nn[::-2]) # 6-9번

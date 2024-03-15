# 연습문제 11번 #


print(int('1011',2))

print(int('1A', 16))

print("----------------------")

# 연습문제 13번 #

print(int('1002',2)) #(1) 오류: 2진수에는 2가 안 들어감.
print(int('1008',8)) #(2) 오류: 8진수에는 8이 안 들어감.
print(int('AAFG', 16)) #(3) 오류: 16진수에는 G가 안 들어감

print("----------------------")

# 연습문제 15번 #

num = 12345678

hex_num = hex(num)
oct_num = oct(num)
bin_num = bin(num)

print("10진수 ==> ", num)
print("16진수 ==> ", hex_num)
print("8진수 ==> ", oct_num)
print("2진수 ==> ", bin_num)

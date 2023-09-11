# 중첩 for, range를 이용하여 구구단 출력하기 
for i in range(2, 10): 
    for j in range(1, 10):
        print(i, "x", j, "=", i*j)

for i in range(2, 10): 
    print(i, "단")
    for j in range(1, 10):
        print(i, "x", j, "=", i*j, end="  ")
    print()
        
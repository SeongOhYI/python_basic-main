# 실행하여 1번을 입력하면 가로형 구구단, 2번을 입력하면 세로형 구구단 
# 3번을 입력하면 종료하는 예제. 
# 각 구구단은 fun1(), fun2() 함수로 정의 
def fun1():
    for i in range(2, 10): 
        for j in range(1, 10):
            print(i, "x", j, "=", i*j)

def fun2():
    for i in range(2, 10): 
        print(i, "단")
        for j in range(1, 10):
            print(i, "x", j, "=", i*j, end="  ")
        print()    

run = True
while run:
    sel = int(input("선택: "))
    if sel == 1:
        fun1()
    elif sel == 2: 
        fun2()
    elif sel == 3:
        print("종료")
        run = False    
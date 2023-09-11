from ex_functions import *

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
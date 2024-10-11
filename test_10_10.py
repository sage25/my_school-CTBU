from random import randint

A_h = 100
A_a = 15
M_h = 100
M_a = 20
temp = 0


while 1:
    print(f"Alice\tHP\t{A_h}\nMonster\tHP\t{M_h}")   
    print("\n")

    #Alice select
    A_input = int(input("请选择:>1.攻击  2.恢复  3.逃跑"))
    #attack
    if A_input == 1:
        if temp == 1:
            M_h -= (0.5*A_a)
            temp -= 1
        else:
            M_h -= A_a
    #recover
    elif A_input == 2:
        if A_h >= 60:
            A_h = 100
        else:
            A_h += 40
    #run
    else:
        num = randint(1,10)
        if num > 7:
            print("逃跑成功")
            break
        else:
            print("逃跑失败")
    #is win
    if M_h <= 0:
        print("胜利")
        break 

    print(f"Alice\tHP\t{A_h}\nMonster\tHP\t{M_h}")  
    print("\n")

    #monster select
    M_input = randint(1,2)
    #attack
    if M_input == 1:
        A_h -= M_a
        print("怪兽选择攻击")
    #defanse
    else:
        temp += 1
        print("怪兽选择防御")

    #is win
    if A_a <= 0:
        print("输了")
        break


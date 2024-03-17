def f1():
    ch = int(input("Введите число "))
    if ch % 3 == 0:
        print("Введенное число делится на 3")
    else:
        print("Введенное число НЕ делится на 3")

def f2():
    try:
        ch=input("Введите число ")
        res=100/int(ch)
        print(res)
    except ValueError:
        print("Ошибка: пожалуйста, введите число")
    except ZeroDivisionError:
        print("Ошибка: на 0 делить нельзя")


def f3():
    dat = input("Введите дату ")
    datnew = dat.split(".")
    den = datnew[0]
    mes = datnew[1]
    god = datnew[2]
    god = god[-2:]
    if int(den) * int(mes) == int(god):
        print("True")
    else:
        print("False")


def f4():
    sperpol = 0
    svtopol = 0
    ch = input("Введите номер билета ")
    if len(ch) % 2 == 0:
        dl = len(ch) // 2
        print(dl)
        perpol = ch[:dl]
        vtopol = ch[-dl:]
        print(perpol, vtopol)
        for i in range(dl):
            sperpol += int(perpol[i])
            svtopol += int(vtopol[i])
        print(sperpol, svtopol)
        if sperpol == svtopol:
            print("Номер является счастливым")
        else:
            print("Номер НЕ является счастливым")
    else:
        print("Перепроверьте введённый номер")


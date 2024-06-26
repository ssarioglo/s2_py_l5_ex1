print("Введите целое число:")
x=int(input())
isNull = False

if x == 0:
    isNull = True
    result="Нулевое число."
elif x < 0:
    otr = "Отрицательное"
else:
    otr = "Положительное"

if x % 2 == 0:
    chet = "четное"
else:
    chet = "нечетное"

if isNull:
    print(result)
else:
    print(otr, chet, "число.")
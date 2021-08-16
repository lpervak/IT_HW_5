def corut_func():
    n = 0
    c = 1
    while True:
        a = yield n / c
        n += a
        c += 1


corut = corut_func()
next(corut)
x = int(input("Enter number: "))
print(corut.send(x))

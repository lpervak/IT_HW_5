def corut():
    n = 0
    c = 1
    while True:
        a = yield n / c
        n += a
        c += 1

cor = corut()
next(cor)
x = int(input("enter number: "))
print(cor.send(x))

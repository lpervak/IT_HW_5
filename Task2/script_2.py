d = int(input("Enter d: "))


def generator_func(d):
    n = 0
    while True:
        yield n
        n += d


generator = generator_func(d)

i = 0

while i < d:
    print(next(generator))
    i += 1

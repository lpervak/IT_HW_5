# fib1 = 1
# fib2 = 1
#
# n = input("number Fib: ")
# n = int(n)
#
# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
#
# print("value :", fib2)

# class Fib:
#     def __init__(self, n):
#         self.n = n
#         self.current = 1
#         self.preview = 1
#
#     def iter(self):
#         return self
#     def __next__(self):
#         if self.current > self.n:
#             raise StopIteration
#         current_1 = self.current + self.preview
#         self.preview, self.current = self.current, current_1
#         return self
#
# fibo = Fib()
# print(fibo)

class Fib:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.n:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib
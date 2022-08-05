a = int(input('Give amount: '))


def fib(n):
    a, b = 0, 1
    for j in range(n):
        yield a
        a, b = b, a + b


for i in list(fib(a)):
    print(i)

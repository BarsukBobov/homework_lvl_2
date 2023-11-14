def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


fib_example = fib()
print(fib_example.__next__())
print(fib_example.__next__())
print(fib_example.__next__())
print(fib_example.__next__())
print(fib_example.__next__())


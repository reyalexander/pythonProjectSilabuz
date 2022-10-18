
def fibonacci(n):
    if n < 0:
        print("El numero debe ser mayor igual a 0")

    elif n < 2:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibiter(x):
    f1 = 1
    f2 = 1
    for i in range(1, int(x) - 1):
        f1, f2 = f2, f1 + f2
    return f2

if __name__ == '__main__':
    print(fibonacci(8))
    print(fibiter(8))

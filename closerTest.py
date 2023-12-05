def calcu():
    a = 3
    b = 10
    def mul(x):
        return a * b * x

    return mul

result1 = calcu()

print(result1(10), result1(100), result1(1000))

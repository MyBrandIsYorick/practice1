def simple(n):
    k = 0
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            k += 1
    if k > 0:
        return True
    else:
        return False


n = int(input("Введите число "))
print([i for i in range(0, n)if simple(i)])

def power(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        result = a*power(a, n-1)
        return result

a = float(input("Введите действительное положительное число a: "))
n = int(input("Введите целое неотрицательное число n: "))
print(power(a, n))
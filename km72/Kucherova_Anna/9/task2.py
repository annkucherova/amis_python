def power(a, n):
    result = pow(a, n)
    return result


a = float(input("Введите действительное положительное число a: "))
n = int(input("Введите целое число n: "))

print(power(a, n))

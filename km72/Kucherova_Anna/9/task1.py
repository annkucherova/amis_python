x1 = float(input("Введите действительное число x1: "))
y1 = float(input("Введите действительное число y1: "))
x2 = float(input("Введите действительное число x2: "))
y2 = float(input("Введите действительное число y2: "))


def distance(x1, y1, x2, y2):
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return dist


print(distance(x1, y1, x2, y2))

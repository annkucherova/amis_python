﻿while True:
  grup1 = int(input("Введіть кількість учнів в першій групі:"))
  grup2 = int(input("Введіть кількість учнів в другій групі:"))
  grup3 = int(input("Введіть кількість учнів в третій групі:"))
  tables = (grup1//2+grup1%2) + (grup2//2 + grup2%2) + (grup3//2 + grup3%2)
  print("Мінiмальна кількість столів - " + str(tables))

print("Здравствуйте")#Выводим приветствие
print("""Данная программа предназначена для решения следующей задачи: Школа формирует три класса.
Какое минимальное количество парт требуется, если за каждой партой
может сидеть не более двух человек?""")#Выводим задачу программы
first_c = int(input("Введите количество ученников в классе №1:"))#Команда для ввода переменной
second_c = int(input("Введите количество ученников в классе №2:"))#Команда для ввода переменной
third_c = int(input("Введите количество ученников в классе №3:"))#Команда для ввода переменной
tables1 = first_c//2 + first_c%2#Посчёт переменной
tables2 = second_c//2 + second_c%2#Посчёт переменной
tables3 = third_c//2 + third_c%2#Посчёт переменной
all_tables = tables1 + tables2 + tables3#Посчёт результатa
print("Минимальное количество столов = " + str(all_tables))#вывод результата
print(input("Нажмите клавишу \"Enter\" для окончания работы программы"))#Команда для окончания программы
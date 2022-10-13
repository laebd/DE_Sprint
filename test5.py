number1 = str(input("Введите первое число в 2ой системе: "))
number2 = str(input("Введите второе число в 2ой системе: "))
intSum = int(number1, 2) + int(number2, 2)
result = bin(intSum)[2:]
print(result)
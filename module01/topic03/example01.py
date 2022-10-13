a = 11
b = 5

# Целочисленные операторы
# Сложение
sum = a + b
print("{} + {} = {}".format(a, b, sum))

# Вычитание
diff = a - b
print("{} - {} = {}".format(a, b, diff))

# Умножение
prod = a * b
print("{} * {} = {}".format(a, b, prod))

# Деление
div = a / b
print("{} / {} = {}".format(a, b, div))

# Целочисленное деление
div_int = a // b
print("{} // {} = {}".format(a, b, div_int))

# Остаток от деления
mod = a % b
print("{} % {} = {}".format(a, b, mod))

# Возведение в степень
exp = a ** b
print("{} в степени {} = {}".format(a, b, exp))

# Порядок выполнения операций
# 1. возведение в степень
# 2. умножение, деление, целочисленное деление и деление по модулю
# 3. сложение и вычитание

# В скобках у операторов выше приоритет 
result = ((a * b) / (a + b)) ** 2
print("Result:", result)
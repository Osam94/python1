def can_break_chocolate(a, b, c):
    if c <= a*b and (c % a == 0 or c % b == 0):
        return "yes"
    else:
        return "no"

a = int(input("Введите ширину шоколадки a: "))
b = int(input("Введите длину шоколадки b: "))
c = int(input("Введите количество долек c: "))

result = can_break_chocolate(a, b, c)
print(result)

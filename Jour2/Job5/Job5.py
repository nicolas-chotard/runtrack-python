def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    else:
        return "Opérateur non valide"

result = calcule(14,"+",34)
print(result)
result = calcule(14, "-" ,34)
print(result)
result = calcule(14, "*" ,34)
print(result)
result = calcule(14, "/" ,34)
print(result)
result = calcule(14, "%" ,34)
print(result)


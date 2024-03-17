# Solution 1 Best Practice
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2
    else:
        return "operador invalido"


# Solucion 2 :)
def basic_op2(operator, value1, value2):
    return eval(f"{value1}{operator}{value2}")


print(basic_op2("+", 4, 7))
print(basic_op2("-", 15, 18))
print(basic_op2("*", 5, 5))
print(basic_op2("/", 49, 7))

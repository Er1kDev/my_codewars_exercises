### 1 segundo son 1.000 milisegundos
### 1 minuto son 60.000 milisegundos
### 1 Hora son 3.600.000 milisegundos


# Solution 1
def past(h, m, s):
    second = 1000
    minute = 60000
    hour = 3600000
    resultado = (h * hour) + (m * minute) + (s * second)
    return resultado


# Solution 2 (Best Practice)
def past(h, m, s):
    return (3600 * h + 60 * m + s) * 1000


print(past(6, 26, 40))

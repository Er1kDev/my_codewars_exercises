def high_and_low(numbers):
    # el list(map(int, numbers.split())) convierte el string
    # en una lista de enteros
    # el max() y min() obtienen el valor maximo y minimo de la lista
    # y se retorna en un string
    # el map() es una funcion que aplica una
    # funcion a cada elemento de una lista
    # el split() separa el string en una lista de strings
    # int convierte el string en un entero
    numbers = list(map(int, numbers.split()))
    return f"{max(numbers)} {min(numbers)}"


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))

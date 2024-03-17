def descending_order(n):
    if n < 0:
        return "no se aceptan numeros negativos"
    elif n == 0:
        return 0
    else:
        return int("".join(sorted(str(n), reverse=True)))


# Explicacion
# La funcion recibe un numero entero
# Si el numero es negativo, la funcion retorna "no se aceptan numeros negativos"
# Si el numero es 0, la funcion retorna 0
# Si el numero es positivo, la funcion convierte el numero
# en un string, lo ordena en orden descendente y lo convierte en un entero
# int() convierte un string en un numero
# str() convierte un numero en un string
# sorted() ordena los elementos de una lista, en este caso, los elementos de un string
# join() convierte una lista en un string
# reverse=True ordena los elementos de la lista en orden descendente

print(descending_order(123456789))

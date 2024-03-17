""" 
Tu objetivo en este kata es implementar una función de diferencia, que resta una lista de otra y devuelve el resultado.

Debería eliminar todos los valores de la lista a, que están presentes en la lista bmanteniendo su orden.
"""

""" def array_diff(a, b):
    return [i for i in a if i not in b] """
""" 
def array_diff(a, b):
    return filter(lambda i: i not in b, a)

filter(function, iterable) devuelve un iterador, por lo que necesitará convertirlo 
en una lista para que coincida con el tipo de retorno esperado.

res = array_diff([1, 2, 3], [1, 2])
print(list(res)) """

""" def array_diff(a, b):
    # your code here
    for i in range(len(b)):
        while b[i] in a:
            a.remove(b[i])
    return a """

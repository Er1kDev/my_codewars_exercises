def longest(s1, s2):
    return "".join(sorted(set(s1 + s2)))


# join es un metodo que une los elementos de una lista en una cadena de texto
# sorted es un metodo que ordena los elementos de una lista
# set es un metodo que elimina los elementos duplicados de una lista
# en este caso se unen las cadenas de texto s1 y s2, se eliminan los elementos
# duplicados y se ordenan los elementos de la lista resultante
# se unen los elementos de la lista resultante en una cadena de texto
# y se retorna la cadena de texto resultante

print(longest("aretheyhere", "yestheyarehere"))

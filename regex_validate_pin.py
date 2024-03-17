"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot 
contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.
"""


# Solution 1
def validate_pin(pin):

    if len(pin) == 4 or len(pin) == 6:
        if pin.isdigit():
            return True
        else:
            return False
    else:
        return False


# isdigit() metodo que verifica si la cadena de texto es un numero

# Solution 2

import re


def validate_pin(pin):
    # return true or false
    return bool(re.fullmatch("\d{4}|\d{6}", pin))


# la funcion fullmatch verifica si la cadena de texto cumple con el patron
# designado, en este caso el patron es que la cadena de texto tenga 4 o 6 digitos
# y que sean numeros.
# el \d{4} verifica que la cadena de texto tenga 4 digitos
# el \d{6} verifica que la cadena de texto tenga 6 digitos
# el | es un operador logico que verifica si la cadena de texto cumple con
# el patron de 4 digitos o 6 digitos


print(validate_pin("-1234"))

# opcion 1
def maskify(cc):

    if len(cc) <= 4:
        return cc
    else:
        return "#" * (len(cc) - 4) + cc[-4:]


# opcion 2
def maskify2(cc):
    return "#" * (len(cc) - 4) + cc[-4:]


print(maskify("12345"))

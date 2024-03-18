def count_sheeps(sheep):
    return sheep.count(True)


""" def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i:
            count += 1
    return count """


array1 = [True, True, True, False, True, False, False]
print(count_sheeps(array1))

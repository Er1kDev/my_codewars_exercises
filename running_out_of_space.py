def spacey(array):
    return ["".join(array[: i + 1]) for i in range(len(array))]


print(spacey(["i", "have", "not", "money"]))

list = ["i", "have", "not", "money"]
for i in range(len(list)):
    print(list[i])

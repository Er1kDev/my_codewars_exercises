def get_middle(word):
    if len(word) % 2 == 1:
        print(word[len(word) // 2])
    elif len(word) % 2 == 0:
        print(word[len(word) // 2 - 1] + word[len(word) // 2])


get_middle("testing")

def is_valid_walk(walk):
    # determine if walk is valid
    if len(walk) != 10:
        return False
    else:
        if walk.count("n") == walk.count("s") and walk.count("w") == walk.count("e"):
            return True
        else:
            return False


print(is_valid_walk(["n", "s", "n", "s", "n", "s", "n", "s", "n", "s"]))


def is_permutation(a: str, b: str) -> bool:
    repetitions = {}

    for char in a:
        if char in repetitions:
            repetitions[char] += 1
        else:
            repetitions[char] = 1

    for char in b:
        if char in repetitions:
            repetitions[char] -= 1
            if repetitions[char] == 0:
                del repetitions[char]
        else:
            return False

    return True


def is_unique(string: str) -> bool:
    for i in range(0, len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False
    return True

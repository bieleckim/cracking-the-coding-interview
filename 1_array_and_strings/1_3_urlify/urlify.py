
def urlify(string: str, length: int) -> str:
    processed = []
    for index in range(0, length):
        if string[index] == ' ':
            processed.append('%20')
        else:
            processed.append(string[index])
    return ''.join(processed)

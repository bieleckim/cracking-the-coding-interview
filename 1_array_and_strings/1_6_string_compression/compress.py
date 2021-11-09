
def compress(string: str) -> str:
    compressed = []
    count = 0

    for index in range(len(string)):
        count += 1
        if index == len(string) - 1 or string[index] != string[index + 1]:
            compressed.append(string[index])
            compressed.append(str(count))
            if len(compressed) > len(string):
                return string
            count = 0
    
    return ''.join(compressed)

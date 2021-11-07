
def is_palindrome_permutation(string: str) -> bool:
    unpaired = {}
    lower = string.lower()
    for char in lower:
        if char == " ":
            continue
        if char in unpaired:
            del unpaired[char]
        else:
            unpaired[char] = True
    return len(unpaired) <= 1

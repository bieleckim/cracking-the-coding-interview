
def is_one_away(a: str, b: str) -> bool:
    if abs(len(a) - len(b)) > 1:
        return False

    a_index = 0
    b_index = 0
    diff = 0
    
    was_replaced = len(a) == len(b)
    was_added = not was_replaced and len(a) + 1 == len(b)
    was_removed = not was_replaced and not was_added

    while a_index < len(a) and b_index < len(b) and diff < 2:
        if a[a_index] != b[b_index]:
            diff += 1
            if was_added:
                a_index -= 1
            if was_removed:
                b_index -= 1
        a_index += 1
        b_index += 1

    return diff < 2

def sequential_search(a_list, item):
    position = 0
    found = False

    while position < len(a_list) and not found:
        if a_list[position] == item:
            found = True
        else:
            position = position + 1
    return found


lists = [1, 2, 45, 65, 32, 78, 98, 64, 12, 89]
print(sequential_search(lists, 100))
print(sequential_search(lists, 98))
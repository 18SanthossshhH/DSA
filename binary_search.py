def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        elif item < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return found


test_list = [12, 23, 36, 45, 52, 65, 78, 84, 98, 102, 124]
print(binary_search(test_list, 36))
print(binary_search(test_list, 68))
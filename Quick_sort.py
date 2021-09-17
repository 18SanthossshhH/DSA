def quick_sort(sequence):
    length = len(sequence)

    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_lower = []
    items_larger = []

    for item in sequence:

        if item > pivot:
            items_larger.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_larger)


print(quick_sort([21, 12, 65, 45, 89, 987, 23, 125, 621, 103, 183]))

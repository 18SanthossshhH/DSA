def merge_sort(a_list):
    print(f"Splitting {a_list}")
    if len(a_list) > 1:
        midpoint = len(a_list) //2
        left_half = a_list[:midpoint]
        right_half = a_list[midpoint:]
        merge_sort(left_half)
        merge_sort(right_half)

        i=0
        j=0
        k=0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[i]:
                a_list[k] = left_half[i]
                i += 1
            else:
                a_list[k] = right_half[i]
                j += 1

            k +=1

            while i < len(left_half):
                a_list[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                a_list[k] = right_half[j]
                j += 1
                k += 1

    print(f'MERGING:  {a_list}')


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(a_list)
print(a_list)

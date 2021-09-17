def bubble_sort(a_list):
    for numbers in range(len(a_list) - 1, 0, -1):
        for i in range(numbers):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]             #This Exhange operation is also known as SWAP
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp


a_list = [24, 36, 12, 9, 85, 46, 65, 89, 98, 78, 45, 23]
bubble_sort(a_list)
print(a_list)

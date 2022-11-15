# Selection Sort Algorithm Implementation
my_list = [3, 5, 7, 2, 34, 8, 90, 0, -2, 78]


def selection_sort(ls):
    for i in range(len(ls)-1):
        for j in range(i, len(ls)):
            if ls[i] > ls[j]:
                ls[i], ls[j] = ls[j], ls[i]
    return ls


print(selection_sort(my_list))